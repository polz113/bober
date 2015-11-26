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
</svg>"""


def generate_award_pdf(output, data, template_file):
    with open(template_file) as f:
        template = f.read()
    shorten_schools(data)
    pages = u"".join(page.format_map(participant) for participant in data)
    cairosvg.svg2pdf(template.format(pages), write_to=output)

def shorten_schools(data):
    replacements = [(u"Osnovna šola", u"OŠ"), (u"Biotehniški izobraževalni center", u"BIC"),
                    (u"Šolski center", u"ŠC"), (u"Srednja šola", u"SŠ")]
    splits = {s.replace("*", " "): s.split("*") for s in
              (u"OŠ Sečovlje*Podružnična šola in vrtec Sveti Peter",
               u"ŠC Kranj,*SŠ za elektrotehniko in računalništvo",
               u"ŠC Novo mesto,*Srednja gradbena, lesarska in vzgojiteljska šola",
               u"ŠC Novo mesto,*Srednja elektro šola in tehniška gimnazija",
               u"OŠ Belokranjskega odreda Semič*Podružnična šola Štrekljevec",
               u"Elektrotehniško-računalniška strokovna*šola in gimnazija Ljubljana",
               u"ŠC Celje,*Srednja šola za kemijo, elektrotehniko in računalništvo",
               u"Zavod Antona Martina Slomška,*Škofijska gimnazija Antona Martina Slomška",
               u"ŠC Krško - Sevnica,*Srednja poklicna in strokovna šola Krško",
               u"Srednja vzgojiteljska šola*in gimnazija Ljubljana",
               u"Gimnazija in srednja šola*Rudolfa Maistra Kamnik",
               u"ŠC za pošto, ekonomijo in telekomunikacije*" \
                   u"Ljubljana, Srednja tehniška in strokovna šola",
               u"OŠ Antona Ingoliča Spodnja Polskava*Podružnica Zgornja Polskava",
               u"ŠC Slovenske Konjice - Zreče,*Gimnazija Slovenske Konjice",
               u"Gimnazija in ekonomska srednja šola*Trbovlje",
               u"Srednja gradbena, geodetska*in okoljevarstvena šola Ljubljana",
               u"OŠ Log - Dragomer,*Podružnična šola Bevke",
               u"OŠ Prežihovega Voranca*Ravne na Koroškem"
               u"Šolski center Nova Gorica,*Gimnazija in zdravstvena šola",
               u"OŠ Franca Lešnika - Vuka*Slivnica pri Mariboru",)
             }

    def short_school(school):
        if len(school) > 30:
            school = reduce(lambda x, r: x.replace(*r), replacements, school)
        if u"Podružnica" in school:
            school = school[:school.index(u"Podružnica") - 1]
        participant["school_x"] = 245.5879 if len(school) < 22 else 136.5879
        participant["school_size"] = 40 if len(school) < 50 else 32
        if school in splits:
            participant["school1"], participant["school2"] = splits[school]
            school = ""
        else:
            participant["school1"] = participant["school2"] = ""
        return school
    for participant in data:
        participant["school"] = short_school(participant["school"])


if __name__ == "__main__":
    N, S, G, E, T = "name", "school", "group", "serial", "template"

    data = [{N: "Gašper Fele Žorž", S: "OŠ Polževo", G: "3. razred", E: "1501999999", T: "bronasto"},
            {N: "Janez Demšar", S: "Vrtec Šentjanž", G: "predšolski", E: "43", T: "priznanje"}]
    certificates(os.path.expanduser("~/Desktop/priznanja.pdf"), data)

    #data = [{N: "Janez Novak", S: s.strip(),
    #         G: "3. razred", E: "42"} for s in open("sole.txt") if len(s) > 45]
    #certificates("priznanje", os.path.expanduser("~/Desktop/test-sol.pdf"), data)
