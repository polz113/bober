#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import cairosvg
import lxml
from io import BytesIO
import uuid
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
                    span = etree.Element('tspan', attrib= attrib)
                    i.append(span)
                span.text = l
            for span in spans[len(lines):]:
                span.text = ''
    return etree.tostring(svg)

def generate_award_pdf_svg(output, data, template_prefix):
    svgs = b'<svg>'
    for d in data:
        t = d['template']
        if len(t) < 1:
            continue
        text_template_filename = os.path.join(template_prefix, t + '.svg')
        with open(text_template_filename, 'r') as f:
            svgs += _data_into_svg(etree.parse(f), d)
    svgs += b'</svg>'
    with open(output + '.svg', 'wb') as f:
        f.write(svgs)
    cairosvg.svg2pdf(svgs, write_to = output)

# what follows is dead code
try:
    import PyPDF2
    from PyPDF2.pdf import ContentStream
    from PyPDF2.generic import DictionaryObject, ArrayObject, NameObject

    def _rename_pdf_resources(res_obj, name_suffix):
        renames = {}
        newResources = DictionaryObject()
        for resource in "/ExtGState", "/Font", "/XObject", "/ColorSpace", "/Pattern", "/Shading", "/Properties":
            newRes = DictionaryObject()
            pageRes = res_obj.get(resource, DictionaryObject()).getObject()
            for key in pageRes.keys():
                newname = NameObject(key + name_suffix)
                newRes[newname] = pageRes.raw_get(key)
                renames[key] = newname
            newResources[NameObject(resource)] = newRes
        # newContent = PyPDF2.ArrayObject()
        newResources[NameObject('/ProcSet')] = res_obj.get('/ProcSet', ArrayObject())
        return newResources, renames

    def _update_resources(dst, src):
        for resource in "/ExtGState", "/Font", "/XObject", "/ColorSpace", "/Pattern", "/Shading", "/Properties":
            name = NameObject(resource)
            i = dst.get(name, DictionaryObject()).getObject()
            i.update(src.get(name, DictionaryObject()).getObject())
            dst[name] = i

    def _rename_isolate_pdf_content(content, renames):
        content.operations.insert(0, [[], "q"])
        for operands, operator in content.operations:
            for i, op in enumerate(operands):
                if isinstance(op, NameObject):
                    operands[i] = renames.get(op, op)
        content.operations.append([[], "Q"])
        return content

    # BEWARE! The function below is useless.
    def generate_award_pdf_pypdf(output, data, template_prefix):
        back_templates = {}
        back_template_resources = DictionaryObject()
        back_template_contents = {}
        text_templates = {}
        out = PyPDF2.PdfFileWriter()
        used_templates = set()
        if len(data) < 1:
            with open(output, 'wb') as out_file:
                out.write(out_file)
            return
        for d in data:
            used_templates.add(d['template'])
        # load the templates
        print("loading templates")
        for t in used_templates:
            back_template_file = os.path.join(template_prefix, t + '.pdf')
            text_template_file = os.path.join(template_prefix, 'front', t + '.svg')
            back_templates[t] = PyPDF2.PdfFileReader(back_template_file).getPage(0)
            with open(text_template_file, 'rb') as f:
                text_templates[t] = etree.parse(f)
        text_pages = []
        # create the overlay PDFs
        print("creating overlays")
        for d in data:
            text_template = text_templates[d['template']]
            text_pages.append(
                PyPDF2.PdfFileReader(
                    BytesIO(cairosvg.svg2pdf(_data_into_svg(text_template, d)))
                ).getPage(0))
        # rename the resources in the templates to avoid clashes
        # then, insert both the resources and the contents of all pages
        # Start by inserting the resources for all back templates into the page tree.
        #   If you do not know what a page tree is, refer to the official 
        # Adobe PDF Reference, Inheritance of Page Attributes
        d = data[0]
        back_template = back_templates[d['template']]
        front_template = text_pages[0]
        box = back_template.mediaBox
        w = box[2] - box[0]
        h = box[3] - box[1]
        page = out.addBlankPage(w, h)
        # insert the back_templates resources into the parent of all pages
        parent = page['/Parent'].getObject()
        # first, rename everything in back_templates, remember the contents
        print("renaming backs")
        for name, back_page in back_templates.items():
            resources, renames = _rename_pdf_resources(back_page['/Resources'].getObject(), name)
            _update_resources(back_template_resources, resources)
            # back_template_resources = resources
            content = ContentStream(back_page.getContents(), page.getObject())
            back_template_contents[name] = _rename_isolate_pdf_content(content, renames)
        contents = ArrayObject()
        contents.append(back_template_contents[d['template']])
        contents.append(front_template['/Contents'])
        # parent[NameObject('/Resources')] = back_template_resources
        page[NameObject('/Resources')] = back_template_resources
        #page.pop(NameObject('/Resources'))
        page[NameObject('/Contents')] = ContentStream(contents, page.pdf)
        print("done")
        for i, d in enumerate(data[1:], start=1):
            print(d)
            back_template = back_templates[d['template']]
            front_template = text_pages[i]
            box = back_template.mediaBox
            w = box[2] - box[0]
            h = box[3] - box[1]
            page = out.addBlankPage(w, h)
            # insert the front_templates resources into the page
            # page.pop(NameObject('/Resources'))
            page[NameObject('/Resources')] = back_template_resources
            
            # construct the content array - first the back
            newContentsArray = ArrayObject()
            newContentsArray.append(back_template_contents[d['template']])
            # and then the front
            newContentsArray.append(front_template['/Contents'])
            page[NameObject('/Contents')] = ContentStream(newContentsArray, page)
        print("writing")
        with open(output, 'wb') as out_file:
            out.write(out_file)
except:
    pass
# end of dead code.

def generate_award_pdf(output, data, template_prefix):
    return generate_award_pdf_svg(output, data, template_prefix)
        

if __name__ == "__main__":
    N, S, G, E, T = "name", "school", "group", "serial", "template"
    data = [{N: u"Gašper Fele Žorž", S: u"OŠ Polževo\nZ dolgim imenom šole\nV mnogih, mnogih, mnooooooooooooogih doooooooooooolgih vrsticah", G: u"3. razred", E: u"1501999999", T: u"bronasto2016", 'date': u'16. november 2016'},
            {N: u"Janez Demšar", S: u"Vrtec Šentjanž", G: u"predšolski", E: u"43", T: u"priznanje2016", 'date': u'16. november 2016'}] 
    data = [ data[i % len(data)].copy() for i in xrange(10)]
    for k, d in enumerate(data):
        d['name'] = "" + d['name'] + str(k)
        print(d['name'], d['template'])
    generate_award_pdf(os.path.expanduser("~/Desktop/priznanja.pdf"), data, 'award_templates/')
            
