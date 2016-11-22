#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from functools import reduce

import cairosvg

# Cairo skips the first text after use. I've no clue why, and I no longer care.
page = u"""
<svg width="1052.36px" height="1488.19px" viewBox="0 0 1052.36 1488.19">
    <use x="0" y="0" xlink:href="#{template}"/>
    <text transform="matrix(1 0 0 1 245.5879 630.623)" fill="#1D1D1B" font-family="'MyriadPro-Regular'; Arial" font-size="48px">
        {name}
    </text>
    <text transform="matrix(1 0 0 1 245.5879 630.623)" fill="#1D1D1B" font-family="'MyriadPro-Regular'; Arial" font-size="48px">
        {name}
    </text>
    <text transform="matrix(1 0 0 1 {school_x} 780.623)" fill="#1D1D1B" font-family="'MyriadPro-Regular'; Arial" font-size="{school_size}px">
        {school}
    </text>
    <text transform="matrix(1 0 0 1 {school_x} 730.623)" fill="#1D1D1B" font-family="'MyriadPro-Regular'; Arial" font-size="{school_size}px">
        {school1}
    </text>
    <text transform="matrix(1 0 0 1 {school_x} 780.623)" fill="#1D1D1B" font-family="'MyriadPro-Regular'; Arial" font-size="{school_size}px">
        {school2}
    </text>
    <text transform="matrix(1 0 0 1 245.5879 943.623)" fill="#3CABE1" font-family="'MyriadPro-Regular'; Arial" font-size="40px">
        {group}
    </text>
    <text transform="matrix(1 0 0 1 848.051 1238.26)" fill="#F9FF7F" font-family="'MyriadPro-Regular'" font-size="9.7082px">
        {serial}
    </text>
    <text transform="matrix(1 0 0 1 370.0 1069.71)" fill="#3CABE0" font-family="'MyriadPro-Regular'; Arial" font-size="32px">
        {date}
    </text>
</svg>"""


def generate_award_pdf(output, data, template_file):
    with open(template_file) as f:
        template = unicode(f.read(), 'utf-8')
    split_schools(data)
    pages = u"".join(page.format(**participant) for participant in data)
    cairosvg.svg2pdf(template.format(pages), write_to=output)

def split_schools(data):
    def split_school(school):
        participant["school_x"] = 245.5879 if len(school) < 22 else 136.5879
        participant["school_size"] = 40 if len(school) < 50 else 32
        split_school = school.split("\n")
        if len(split_school) > 1:
            participant["school1"] = split_school[0]
            participant["school2"] = " ".join(split_school[1:])
            school = ""
        else:
            participant["school1"] = participant["school2"] = ""
        return school
    for participant in data:
        participant["school"] = split_school(participant["school"])


if __name__ == "__main__":
    N, S, G, E, T = "name", "school", "group", "serial", "template"

    data = [{N: u"Gašper Fele Žorž", S: u"OŠ Polževo", G: u"3. razred", E: u"1501999999", T: u"bronasto2016", 'date': u'16. november 2016'},
            {N: u"Janez Demšar", S: u"Vrtec Šentjanž", G: u"predšolski", E: u"43", T: u"priznanje2016", 'date': u'16. november 2016'}]
    generate_award_pdf(os.path.expanduser("~/Desktop/priznanja.pdf"), data, 'award_templates/all_si.svg')

    #data = [{N: "Janez Novak", S: s.strip(),
    #         G: "3. razred", E: "42"} for s in open("sole.txt") if len(s) > 45]
    #certificates("priznanje", os.path.expanduser("~/Desktop/test-sol.pdf"), data)
