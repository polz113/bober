import os
# import cairosvg
import cairocffi
from cairosvg.parser import Tree
from cairosvg.surface import PDFSurface
from lxml import etree


def _data_into_svg(svg, data):
    for k, v in data.items():
        if v is None:
            v = ''
        t = svg.xpath(u"//node()[@id='{}']".format(k))
        for i in t:
            i.text = ''
            lines = v.split('\n')
            spans = list(i.findall('{http://www.w3.org/2000/svg}tspan'))
            # print i, list(i), spans
            attrib = {}
            for n, l in enumerate(lines):
                if len(spans) > n:
                    span = spans[n]
                    attrib = span.attrib
                else:
                    span = etree.Element('tspan', attrib=attrib)
                    i.append(span)
                span.text = l
            for span in spans[len(lines):]:
                span.text = ''
    return svg


def generate_award_pdf_svg(output, data, template_prefix, dpi=96):
    svgs = []
    surface = cairocffi.PDFSurface(output, 1, 1)
    context = cairocffi.Context(surface)
    for d in data:
        t = d['template']
        if len(t) < 1:
            continue
        text_template_filename = os.path.join(template_prefix, t + '.svg')
        with open(text_template_filename, 'r') as f:
            svg = etree.parse(f)
        svg = _data_into_svg(svg, d)
        svg_str = etree.tostring(svg)
        tree = Tree(bytestring=svg_str)
        svgs.append(svg_str)
        image_surface = PDFSurface(tree, None, dpi)
        surface.set_size(image_surface.width, image_surface.height)
        context.set_source_surface(image_surface.cairo, 0, 0)
        context.paint()
        surface.show_page()
        # with open(text_template_filename, 'r') as f:
        #    svgs.append(_data_into_svg(etree.parse(f), d))
    # svgs += b'</svg>'
    surface.finish()
    with open(output + '.svg', 'wb') as f:
        f.write(b"\n".join(svgs))
    # cairosvg.svg2pdf(svgs, write_to=output)  # @UndefinedVariable


def generate_award_pdf(output, data, template_prefix):
    return generate_award_pdf_svg(output, data, template_prefix)


if __name__ == "__main__":
    N, S, G, E, T = "name", "school", "group", "serial", "template"
    data = [{N: u"Gašper Fele Žorž",
             S: u"OŠ Polževo\nZ dolgim imenom šole\nV mnogih, mnogih, mnooooooooooooogih doooooooooooolgih vrsticah",
             G: u"3. razred", E: u"1501999999", T: u"bronasto2016", 'date': u'16. november 2016'},
            {N: u"Janez Demšar", S: u"Vrtec Šentjanž", G: u"predšolski", E: u"43", T: u"priznanje2016",
             'date': u'16. november 2016'}]
    data = [data[i % len(data)].copy() for i in range(10)]
    for k, d in enumerate(data):
        d['name'] = "" + d['name'] + str(k)
        print(d['name'], d['template'])
    generate_award_pdf(os.path.expanduser("~/Desktop/priznanja.pdf"), data, 'award_templates/')
