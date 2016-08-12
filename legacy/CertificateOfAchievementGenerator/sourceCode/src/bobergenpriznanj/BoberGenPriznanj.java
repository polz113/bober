package bobergenpriznanj;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author Gregor Kužnik
 */
public class BoberGenPriznanj {

    public List<Mentor> mentorji = new ArrayList<Mentor>();
    public List<String> csvBrisanje = new ArrayList<String>();

    public static void main(String[] args) throws IOException, InterruptedException {
        BoberGenPriznanj inst = new BoberGenPriznanj();

        //Branje nastavitev
        File nastavitve = new File("nastavitve.ini");
        boolean solsko = false;
        boolean drzavno = false;
        boolean drzavnoUspeh = false;

        if (!nastavitve.exists()) {
            System.out.println("Manjka datoteka \"nastavitve.ini\"");
        } else {
            BufferedReader branje = new BufferedReader(new InputStreamReader(new FileInputStream(nastavitve), "UTF-8"));
            String vrstica;
            String vrsticaSplit[];
            for (int i = 0; i < 3; i++) {
                vrstica = branje.readLine();
                vrsticaSplit = vrstica.split("=");
                if (vrsticaSplit[0].equals("Solsko") && vrsticaSplit[1].equals("1")) {
                    solsko = true;
                } else if (vrsticaSplit[0].equals("Drzavno") && vrsticaSplit[1].equals("1")) {
                    drzavno = true;
                } else if (vrsticaSplit[0].equals("DrzavnoUspeh") && vrsticaSplit[1].equals("1")) {
                    drzavnoUspeh = true;
                }
            }
        }

        //Generiraj mapo Priznanja ce se ne obstaja
        File priznanja = new File("Priznanja");
        if (!priznanja.exists()) {
            priznanja.mkdir();
        }
        File testCSV = new File("PodatkiCSV");
        File testPDF = new File("PodatkiPDF");
        if (!testCSV.exists() || !testPDF.exists()) {
            System.out.println("Manjkajo nekatere mape oz. podatki");
        } else {
            //Bober priznanja solsko
            if (solsko) {
                inst.preberiCSV("PodatkiCSV/Solsko/bober.csv", 0);
                inst.preberiCSV("PodatkiCSV/Solsko/bobrcek.csv", 1);
                inst.preberiCSV("PodatkiCSV/Solsko/mladi_bober.csv", 2);
                inst.preberiCSV("PodatkiCSV/Solsko/stari_bober.csv", 3);
                System.out.println("Branje solsko koncano");
                inst.generirajSolsko();
                System.out.println("Generiranje tekmovalci solsko koncano");
                inst.generirajMentorSolsko();
                System.out.println("Generiranje mentor solsko koncano");
            }
            //Bober priznanja drzavno
            if (drzavno) {
                inst.preberiCSV("PodatkiCSV/Drzavno/bober.csv", 0);
                inst.preberiCSV("PodatkiCSV/Drzavno/bobrcek.csv", 1);
                inst.preberiCSV("PodatkiCSV/Drzavno/mladi_bober.csv", 2);
                inst.preberiCSV("PodatkiCSV/Drzavno/stari_bober.csv", 3);
                System.out.println("Branje drzavno koncano");
                inst.generirajDrzavno();
                System.out.println("Generiranje tekmovalci drzavno koncano");
                inst.generirajMentorDrzavno();
                System.out.println("Generiranje mentor drzavno koncano");
            }
            //Bober priznanja drzavno uspeh
            if (drzavnoUspeh) {
                inst.preberiDrzavnoUspeh("PodatkiCSV/Drzavno/skupni_rezultati.csv");
                System.out.println("Branje drzavno skupni rezultati koncano");
                inst.generirajDrzavnoMentorUspeh();
                System.out.println("Generiranje drzavno skupni rezultati koncano");
            }
            //Brisanje csv datotek
            inst.pobrisiCSV();
            new File("settings.ini").deleteOnExit();
        }
    }

    public void pobrisiCSV() throws InterruptedException {
        //Da se csvji ne pobrisejo preden se zgenerira PDF
        Thread.sleep(10000);
        for (String s : csvBrisanje) {
            File f = new File(s);
            f.deleteOnExit();
        }
    }

    public void preberiDrzavnoUspeh(String vhodniCSV) throws IOException {
        BufferedReader branje = new BufferedReader(new InputStreamReader(new FileInputStream(vhodniCSV), "UTF-8"));
        String vrstica;
        //Spusti prvo vrstico (header)
        branje.readLine();
        String trenutniMentorId = "-1";
        Mentor mentor = null;

        //Branje podatkov
        while ((vrstica = branje.readLine()) != null) {
            String[] vrsticaSplit = vrstica.split(";");
            String mentorId = vrsticaSplit[2];

            boolean obstaja = false;
            for (Mentor m : mentorji) {
                if (m.getId().equals(mentorId)) {
                    mentor = m;
                    obstaja = true;
                    break;
                }
            }
            if (!obstaja) {
                //"Nov" mentor
                String sola = vrsticaSplit[10];
                String mentorIme = vrsticaSplit[1];
                mentor = new Mentor(mentorId, sola, mentorIme, new ArrayList<Tekmovalec>());
                mentorji.add(mentor);
            }

            String tekmovalecId = "-1";
            String tekmovalecIme = vrsticaSplit[12] + " " + vrsticaSplit[13];
            //0-bronasto,1-srebrno,2-zlato,-1-prazno
            String priznanje = vrsticaSplit[7];
            int priznanjeInt = Integer.parseInt(priznanje);

            Tekmovalec tekmovalec = new Tekmovalec(tekmovalecId, tekmovalecIme, priznanjeInt, -1);
            mentor.getTekmovalci().add(tekmovalec);
        }
    }

    public void generirajDrzavnoMentorUspeh() throws InterruptedException, IOException {
        String mentorHeader = "\"Mentor\";\"Šola\";\"Srebrna\";\"Zlata\"";
        String CSVmentor = "Priznanja/priznanje_mentor_drzavno_uspeh.csv";
        BufferedWriter wMentor = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(CSVmentor, false), "UTF-8"));
        wMentor.append(mentorHeader);
        wMentor.append('\n');
        wMentor.flush();

        for (Mentor m : mentorji) {

            int mentorId = Integer.parseInt(m.getId());
            String sola = m.getSola();
            String mentorIme = m.getIme();
            String srebrna = m.countSrebrna();
            String zlata = m.countZlata();

            wMentor.append("\"" + mentorIme + "\";\"" + sola + "\";\"Srebrna priznanja: " + srebrna + "\";\"Zlata priznanja: " + zlata + "\"");
            wMentor.append("\n");
            wMentor.flush();
        }
        wMentor.close();

        zapisiMentorDrzavnoUspehSettings();
        File f = new File("Priznanja/priznanje_mentor_drzavno_uspeh.pdf");
        while (true) {
            if (f.exists()) {
                break;
            }
            Process p = Runtime.getRuntime().exec("java -jar csv-pdf_1_42.jar");
            p.waitFor();
        }
        csvBrisanje.add("Priznanja/priznanje_mentor_drzavno_uspeh.csv");
    }

    public void generirajMentorDrzavno() throws IOException, InterruptedException {
        String mentorHeader = "\"Mentor\";\"Šola\";\"Tekmovalci\"";
        String CSVmentor = "Priznanja/priznanje_mentor_drzavno.csv";
        BufferedWriter wMentor = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(CSVmentor, false), "UTF-8"));
        wMentor.append(mentorHeader);
        wMentor.append('\n');
        wMentor.flush();

        for (Mentor m : mentorji) {

            int mentorId = Integer.parseInt(m.getId());
            String sola = m.getSola();
            String mentorIme = m.getIme();

            wMentor.append("\"" + mentorIme + "\";\"" + sola + "\";\"" + m.tekmovalciToString() + "\"");
            wMentor.append("\n");
            wMentor.flush();
        }
        wMentor.close();

        zapisiMentorDrzavnoSettings();
        File f = new File("Priznanja/priznanje_mentor_drzavno.pdf");
        while (true) {
            if (f.exists()) {
                break;
            }
            Process p = Runtime.getRuntime().exec("java -jar csv-pdf_1_42.jar");
            p.waitFor();
        }
        csvBrisanje.add("Priznanja/priznanje_mentor_drzavno.csv");
        mentorji.clear();
    }

    public void generirajDrzavno() throws IOException, InterruptedException {
        String tekmovalecHeader = "\"Priimek in Ime\";\"Šola\"";
        String seznamHeader = "\"ID\";\"Priimek in Ime\";\"Zap. št. priznanja\"";
        String kategorije[] = {"bober", "bobrcek", "mladi_bober", "stari_bober"};

        String seznam = "Priznanja/seznam_zlato-srebrno.csv";
        BufferedWriter wSeznam = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(seznam, false), "UTF-8"));
        wSeznam.append(seznamHeader);
        wSeznam.append('\n');
        wSeznam.flush();

        int stevecOut[] = {1, 1, 1, 1};

        for (Mentor m : mentorji) {

            int stevecIn[] = {0, 0, 0, 0};
            int mentorId = Integer.parseInt(m.getId());
            String sola = m.getSola();

            //Tekmovalci
            for (Tekmovalec t : m.getTekmovalci()) {
                String TekmovalecIme = t.getIme();
                String TekmovalecId = t.getId();
                int k = t.getKategorija();

                String CSVudel = "Priznanja/priznanje_za_udelezbo_drzavno-" + kategorije[k] + ".csv";
                BufferedWriter wUdel;

                if (!(new File(CSVudel)).exists()) {
                    wUdel = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(CSVudel, true), "UTF-8"));
                    wUdel.append(tekmovalecHeader);
                    wUdel.append('\n');
                    wUdel.flush();
                } else {
                    wUdel = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(CSVudel, true), "UTF-8"));
                }

                wUdel.append("\"" + TekmovalecIme + "\";\"" + sola + "\"");
                wUdel.append("\n");
                wUdel.flush();
                wUdel.close();

                //Srebrno-zlato
                String CSVsreb = "Priznanja/priznanje_srebrno-" + kategorije[k] + ".csv";
                String CSVzlat = "Priznanja/priznanje_zlato-" + kategorije[k] + ".csv";

                BufferedWriter wSreb;
                BufferedWriter wZlat;

                if (!(new File(CSVsreb)).exists()) {
                    wSreb = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(CSVsreb, true), "UTF-8"));
                    wSreb.append(tekmovalecHeader);
                    wSreb.append('\n');
                    wSreb.flush();
                } else {
                    wSreb = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(CSVsreb, true), "UTF-8"));
                }
                wSreb.append("\"" + TekmovalecIme + "\";\"" + sola + "\"");
                wSreb.append('\n');
                wSreb.flush();
                wSreb.close();

                if (!(new File(CSVzlat)).exists()) {
                    wZlat = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(CSVzlat, true), "UTF-8"));
                    wZlat.append(tekmovalecHeader);
                    wZlat.append('\n');
                    wZlat.flush();
                } else {
                    wZlat = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(CSVzlat, true), "UTF-8"));
                }
                wZlat.append("\"" + TekmovalecIme + "\";\"" + sola + "\"");
                wZlat.append('\n');
                wZlat.flush();
                wZlat.close();

                wSeznam.append(TekmovalecId + "\";\"" + TekmovalecIme + "\";\"" + (stevecOut[k] + stevecIn[k]) + "\"");
                wSeznam.append('\n');
                wSeznam.flush();
                stevecIn[k]++;
            }
            for (int i = 0; i < 4; i++) {
                stevecOut[i] += stevecIn[i];
            }
        }
        wSeznam.close();

        //Zgeneriraj
        for (int i = 0; i < 4; i++) {
            zapisiDrzavnoSettings(kategorije[i]);
            File f = new File("Priznanja/priznanje_za_udelezbo_drzavno-" + kategorije[i] + ".pdf");
            while (true) {
                if (f.exists()) {
                    break;
                }
                Process p = Runtime.getRuntime().exec("java -jar csv-pdf_1_42.jar");
                p.waitFor();
            }
            csvBrisanje.add("Priznanja/priznanje_za_udelezbo_drzavno-" + kategorije[i] + ".csv");
        }
        for (int i = 0; i < 4; i++) {
            zapisiSrebrnoSettings(kategorije[i]);
            File f = new File("Priznanja/priznanje_srebrno-" + kategorije[i] + ".pdf");
            while (true) {
                if (f.exists()) {
                    break;
                }
                Process p = Runtime.getRuntime().exec("java -jar csv-pdf_1_42.jar");
                p.waitFor();
            }
            csvBrisanje.add("Priznanja/priznanje_srebrno-" + kategorije[i] + ".csv");
        }
        for (int i = 0; i < 4; i++) {
            zapisiZlatoSettings(kategorije[i]);
            File f = new File("Priznanja/priznanje_zlato-" + kategorije[i] + ".pdf");
            while (true) {
                if (f.exists()) {
                    break;
                }
                Process p = Runtime.getRuntime().exec("java -jar csv-pdf_1_42.jar");
                p.waitFor();
            }
            csvBrisanje.add("Priznanja/priznanje_zlato-" + kategorije[i] + ".csv");
        }

    }

    public void generirajMentorSolsko() throws IOException, InterruptedException {
        String mentorHeader = "\"Mentor\";\"Šola\";\"Tekmovalci\"";
        for (Mentor m : mentorji) {

            int mentorId = Integer.parseInt(m.getId());
            String sola = m.getSola();
            String mentorIme = m.getIme();
            int steviloTek = m.getTekmovalci().size();

            //Mentor
            String CSVmentor = "Priznanja/" + mentorId + "/priznanje_mentor.csv";
            BufferedWriter wMentor = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(CSVmentor, false), "UTF-8"));
            wMentor.append(mentorHeader);
            wMentor.append('\n');
            wMentor.append("\"" + mentorIme + "\";\"" + sola + "\";\"mentorstvo za " + steviloTek + " udeležencev na šolskem tekmovanju\"");
            wMentor.flush();
            wMentor.close();

            zapisiMentorSolskoSettings(mentorId);
            File f = new File("Priznanja/" + mentorId + "/priznanje_mentor.pdf");
            while (true) {
                if (f.exists()) {
                    break;
                }
                Process p = Runtime.getRuntime().exec("java -jar csv-pdf_1_42.jar");
                p.waitFor();
            }
            csvBrisanje.add("Priznanja/" + mentorId + "/priznanje_mentor.csv");
        }
        mentorji.clear();
    }

    public void generirajSolsko() throws IOException, InterruptedException {
        String tekmovalecHeader = "\"Priimek in Ime\";\"Šola\"";
        String seznamHeader = "\"ID\";\"Priimek in Ime\";\"Zap. št. priznanja\"";
        String kategorije[] = {"bober", "bobrcek", "mladi_bober", "stari_bober"};

        String seznam = "Priznanja/seznam_bronasto.csv";
        BufferedWriter wSeznam = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(seznam, false), "UTF-8"));
        wSeznam.append(seznamHeader);
        wSeznam.append('\n');
        wSeznam.flush();

        int stevecOut[] = {1, 1, 1, 1};
        List<int[]> zaGenerirati = new ArrayList<int[]>();

        for (Mentor m : mentorji) {

            int stevecIn[] = {0, 0, 0, 0};
            int mentorId = Integer.parseInt(m.getId());
            String sola = m.getSola();

            File direktorij = new File("Priznanja/" + mentorId + "");
            if (!direktorij.exists()) {
                if (!direktorij.mkdir()) {
                    System.out.println("Napaka pri ustvarjanju direktorija!");
                }
            }

            //Tekmovalci
            for (Tekmovalec t : m.getTekmovalci()) {
                String TekmovalecIme = t.getIme();
                String TekmovalecId = t.getId();
                int priznanje = t.getPriznanje();
                int k = t.getKategorija();

                String CSVudel = "Priznanja/" + mentorId + "/priznanje_za_udelezbo-" + kategorije[k] + ".csv";
                BufferedWriter wUdel;

                if (!(new File(CSVudel)).exists()) {
                    wUdel = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(CSVudel, true), "UTF-8"));
                    wUdel.append(tekmovalecHeader);
                    wUdel.append('\n');
                    wUdel.flush();
                    int gen[] = {k, mentorId, -1};
                    zaGenerirati.add(gen);
                } else {
                    wUdel = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(CSVudel, true), "UTF-8"));
                }
                wUdel.append("\"" + TekmovalecIme + "\";\"" + sola + "\"");
                wUdel.append("\n");
                wUdel.flush();
                wUdel.close();

                //Bron
                if (priznanje == 0) {
                    String CSVbron = "Priznanja/" + mentorId + "/priznanje_bronasto-" + kategorije[k] + ".csv";
                    BufferedWriter wBron;

                    if (!(new File(CSVbron)).exists()) {
                        wBron = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(CSVbron, true), "UTF-8"));
                        wBron.append(tekmovalecHeader);
                        wBron.append('\n');
                        wBron.flush();
                        int gen[] = {k, mentorId, stevecOut[k]};
                        zaGenerirati.add(gen);
                    } else {
                        wBron = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(CSVbron, true), "UTF-8"));
                    }
                    wBron.append("\"" + TekmovalecIme + "\";\"" + sola + "\"");
                    wBron.append('\n');
                    wBron.flush();
                    wBron.close();

                    wSeznam.append(TekmovalecId + "\";\"" + TekmovalecIme + "\";\"" + (stevecOut[k] + stevecIn[k]) + "\"");
                    wSeznam.append('\n');
                    wSeznam.flush();
                    stevecIn[k]++;
                }
            }
            for (int[] gen : zaGenerirati) {
                if (gen[2] == -1) {
                    zapisiSettings(kategorije[gen[0]], gen[1]);
                    File f = new File("Priznanja/" + mentorId + "/priznanje_za_udelezbo-" + kategorije[gen[0]] + ".pdf");
                    while (true) {
                        if (f.exists()) {
                            break;
                        }
                        Process p = Runtime.getRuntime().exec("java -jar csv-pdf_1_42.jar");
                        p.waitFor();
                    }
                    csvBrisanje.add("Priznanja/" + mentorId + "/priznanje_za_udelezbo-" + kategorije[gen[0]] + ".csv");

                } else {
                    zapisiBronSettings(kategorije[gen[0]], gen[1], gen[2]);
                    File f = new File("Priznanja/" + mentorId + "/priznanje_bronasto-" + kategorije[gen[0]] + ".pdf");
                    while (true) {
                        if (f.exists()) {
                            break;
                        }
                        Process p = Runtime.getRuntime().exec("java -jar csv-pdf_1_42.jar");
                        p.waitFor();
                    }
                    csvBrisanje.add("Priznanja/" + mentorId + "/priznanje_bronasto-" + kategorije[gen[0]] + ".csv");
                }
            }
            zaGenerirati.clear();
            for (int i = 0; i < 4; i++) {
                stevecOut[i] += stevecIn[i];
            }
        }
        wSeznam.close();
    }

    public void preberiCSV(String vhodniCSV, int kategorija) throws IOException {
        BufferedReader branje = new BufferedReader(new InputStreamReader(new FileInputStream(vhodniCSV), "UTF-8"));
        String vrstica;
        //Spusti prvo vrstico (header)
        branje.readLine();
        String trenutniMentorId = "-1";
        Mentor mentor = null;

        //Branje podatkov
        while ((vrstica = branje.readLine()) != null) {
            String[] vrsticaSplit = vrstica.split("\";\"");
            if (vrsticaSplit[10].equals("Da")) {
                continue;
            }
            String mentorId = vrsticaSplit[4];

            boolean obstaja = false;
            for (Mentor m : mentorji) {
                if (m.getId().equals(mentorId)) {
                    mentor = m;
                    obstaja = true;
                    break;
                }
            }
            if (!obstaja) {
                //"Nov" mentor
                String sola = vrsticaSplit[2];
                String mentorIme = vrsticaSplit[3];
                mentor = new Mentor(mentorId, sola, mentorIme, new ArrayList<Tekmovalec>());
                mentorji.add(mentor);
            }

            String tekmovalecId = vrsticaSplit[0];
            String tekmovalecIme = vrsticaSplit[7] + " " + vrsticaSplit[8];
            //0-bronasto,1-srebrno,2-zlato,-1-prazno
            String priznanje = vrsticaSplit[vrsticaSplit.length - 2];
            int priznanjeInt = -1;
            if (priznanje.equals("Bronasto priznanje")) {
                priznanjeInt = 0;
            }

            Tekmovalec tekmovalec = new Tekmovalec(tekmovalecId, tekmovalecIme, priznanjeInt, kategorija);
            mentor.getTekmovalci().add(tekmovalec);
        }
    }

    public static void zapisiSettings(String kategorija, int mentorId) throws IOException {
        String settings = "csvFile=Priznanja/" + mentorId + "/priznanje_za_udelezbo-" + kategorija + ".csv\n"
                + "pdfTemplate=PodatkiPDF/Priznanje/" + kategorija + ".pdf\n"
                + "csvDelimiter=\";\"\n"
                + "singlePage=false\n"
                + "pdfResult=Priznanja/" + mentorId + "/priznanje_za_udelezbo-" + kategorija + ".pdf\n"
                + "counter=-1;0\n"
                + "line1=Priimek in Ime;295;473;22;Helvetica;0;0;0;1\n"
                + "lines=1\n"
                + "block1=Šola;100;300;550;405;22;Helvetica;0;0;0;1\n"
                + "blocks=1";

        String urlSettings = "settings.ini";
        BufferedWriter wSettings = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(urlSettings, false), "UTF-8"));
        wSettings.write(settings);
        wSettings.flush();
        wSettings.close();
    }

    public static void zapisiBronSettings(String kategorija, int mentorId, int stevec) throws IOException {

        String settings = "csvFile=Priznanja/" + mentorId + "/priznanje_bronasto-" + kategorija + ".csv\n"
                + "pdfTemplate=PodatkiPDF/Priznanje_bronasto/" + kategorija + ".pdf\n"
                + "csvDelimiter=\";\"\n"
                + "singlePage=false\n"
                + "pdfResult=Priznanja/" + mentorId + "/priznanje_bronasto-" + kategorija + ".pdf\n"
                + "counter=" + stevec + ";514;150;20;Helvetica;0;0;0;1\n"
                + "line1=Priimek in Ime;295;473;22;Helvetica;0;0;0;1\n"
                + "lines=1\n"
                + "block1=Šola;100;300;550;405;22;Helvetica;0;0;0;1\n"
                + "blocks=1";

        String urlSettings = "settings.ini";
        BufferedWriter wSettings = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(urlSettings, false), "UTF-8"));
        wSettings.write(settings);
        wSettings.flush();
        wSettings.close();
    }

    public static void zapisiMentorSolskoSettings(int mentorId) throws IOException {
        String settings = "csvFile=Priznanja/" + mentorId + "/priznanje_mentor.csv\n"
                + "pdfTemplate=PodatkiPDF/Potrdilo_mentorji/potrdilo.pdf\n"
                + "csvDelimiter=\";\"\n"
                + "singlePage=false\n"
                + "pdfResult=Priznanja/" + mentorId + "/priznanje_mentor.pdf\n"
                + "counter=-1\n"
                + "line1=Mentor;200;582;22;Helvetica;0;0;0;1\n"
                + "lines=1\n"
                + "block1=Šola;100;440;530;490;22;Helvetica;0;0;0;1\n"
                + "block2=Tekmovalci;140;240;530;403;22;Helvetica;0;0;0;1\n"
                + "blocks=2";

        String urlSettings = "settings.ini";
        BufferedWriter wSettings = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(urlSettings, false), "UTF-8"));
        wSettings.write(settings);
        wSettings.flush();
        wSettings.close();
    }

    public static void zapisiDrzavnoSettings(String kategorija) throws IOException {
        String settings = "csvFile=Priznanja/priznanje_za_udelezbo_drzavno-" + kategorija + ".csv\n"
                + "pdfTemplate=PodatkiPDF/Priznanje_udelezba_finale/" + kategorija + ".pdf\n"
                + "csvDelimiter=\";\"\n"
                + "singlePage=false\n"
                + "pdfResult=Priznanja/priznanje_za_udelezbo_drzavno-" + kategorija + ".pdf\n"
                + "counter=-1\n"
                + "line1=Priimek in Ime;295;473;22;Helvetica;0;0;0;1\n"
                + "lines=1\n"
                + "block1=Šola;100;300;550;405;22;Helvetica;0;0;0;1\n"
                + "blocks=1";

        String urlSettings = "settings.ini";
        BufferedWriter wSettings = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(urlSettings, false), "UTF-8"));
        wSettings.write(settings);
        wSettings.flush();
        wSettings.close();
    }

    public static void zapisiSrebrnoSettings(String kategorija) throws IOException {
        String settings = "csvFile=Priznanja/priznanje_srebrno-" + kategorija + ".csv\n"
                + "pdfTemplate=PodatkiPDF/Priznanje_srebrno/" + kategorija + ".pdf\n"
                + "csvDelimiter=\";\"\n"
                + "singlePage=false\n"
                + "pdfResult=Priznanja/priznanje_srebrno-" + kategorija + ".pdf\n"
                + "counter=1;514;150;20;Helvetica;0;0;0;1\n"
                + "line1=Priimek in Ime;295;473;22;Helvetica;0;0;0;1\n"
                + "lines=1\n"
                + "block1=Šola;100;300;550;405;22;Helvetica;0;0;0;1\n"
                + "blocks=1";

        String urlSettings = "settings.ini";
        BufferedWriter wSettings = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(urlSettings, false), "UTF-8"));
        wSettings.write(settings);
        wSettings.flush();
        wSettings.close();
    }

    public static void zapisiZlatoSettings(String kategorija) throws IOException {
        String settings = "csvFile=Priznanja/priznanje_zlato-" + kategorija + ".csv\n"
                + "pdfTemplate=PodatkiPDF/Priznanje_zlato/" + kategorija + ".pdf\n"
                + "csvDelimiter=\";\"\n"
                + "singlePage=false\n"
                + "pdfResult=Priznanja/priznanje_zlato-" + kategorija + ".pdf\n"
                + "counter=1;514;150;20;Helvetica;0;0;0;1\n"
                + "line1=Priimek in Ime;295;473;22;Helvetica;0;0;0;1\n"
                + "lines=1\n"
                + "block1=Šola;100;300;550;405;22;Helvetica;0;0;0;1\n"
                + "blocks=1";

        String urlSettings = "settings.ini";
        BufferedWriter wSettings = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(urlSettings, false), "UTF-8"));
        wSettings.write(settings);
        wSettings.flush();
        wSettings.close();
    }

    public static void zapisiMentorDrzavnoSettings() throws IOException {
        String settings = "csvFile=Priznanja/priznanje_mentor_drzavno.csv\n"
                + "pdfTemplate=PodatkiPDF/Potrdilo_mentorji_drzavno_udelezba/potrdilo-udelezba.pdf\n"
                + "csvDelimiter=\";\"\n"
                + "singlePage=false\n"
                + "pdfResult=Priznanja/priznanje_mentor_drzavno.pdf\n"
                + "counter=-1\n"
                + "line1=Mentor;295;524;22;Helvetica;0;0;0;1\n"
                + "lines=1\n"
                + "block1=Šola;100;440;520;485;22;Helvetica;0;0;0;1\n"
                + "block2=Tekmovalci;150;150;500;410;18;Helvetica;0;0;0;0\n"
                + "blocks=2";

        String urlSettings = "settings.ini";
        BufferedWriter wSettings = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(urlSettings, false), "UTF-8"));
        wSettings.write(settings);
        wSettings.flush();
        wSettings.close();
    }

    public static void zapisiMentorDrzavnoUspehSettings() throws IOException {
        String settings = "csvFile=Priznanja/priznanje_mentor_drzavno_uspeh.csv\n"
                + "pdfTemplate=PodatkiPDF/Potrdila_mentorji_drzavno_uspeh/potrdilo-uspeh.pdf\n"
                + "csvDelimiter=\";\"\n"
                + "singlePage=false\n"
                + "pdfResult=Priznanja/priznanje_mentor_drzavno_uspeh.pdf\n"
                + "counter=-1\n"
                + "line1=Mentor;295;524;22;Helvetica;0;0;0;1\n"
                + "line2=Srebrna;170;360;22;Helvetica;0;0;0;0\n"
                + "line3=Zlata;170;320;22;Helvetica;0;0;0;0\n"
                + "lines=3\n"
                + "block1=Šola;100;440;500;485;22;Helvetica;0;0;0;1\n"
                + "blocks=1";

        String urlSettings = "settings.ini";
        BufferedWriter wSettings = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(urlSettings, false), "UTF-8"));
        wSettings.write(settings);
        wSettings.flush();
        wSettings.close();
    }
}

class Mentor {

    private String id;
    private String sola;
    private String ime;
    private List<Tekmovalec> tekmovalci;

    public Mentor(String id, String sola, String ime, List<Tekmovalec> tekmovalci) {
        this.id = id;
        this.sola = sola;
        this.ime = ime;
        this.tekmovalci = tekmovalci;
    }

    //Get
    public String getId() {
        return id;
    }

    public String getSola() {
        return sola;
    }

    public String getIme() {
        return ime;
    }

    public List<Tekmovalec> getTekmovalci() {
        return tekmovalci;
    }

    //Set
    public void setTekmovalci(List<Tekmovalec> tekmovalci) {
        this.tekmovalci = tekmovalci;
    }

    //Ostale metode
    public String tekmovalciToString() {
        StringBuilder sb = new StringBuilder();
        for (Tekmovalec t : this.tekmovalci) {
            sb.append(t.toString() + ", ");
        }
        sb.deleteCharAt(sb.length() - 1);
        sb.deleteCharAt(sb.length() - 1);
        String out = sb.toString();
        return out;
    }

    public String countSrebrna() {
        int stevec = 0;
        for (Tekmovalec t : this.tekmovalci) {
            if (t.getPriznanje() == 2) {
                stevec++;
            }
        }
        if (stevec == 0) {
            return "/";
        } else {
            return stevec + "";
        }
    }

    public String countZlata() {
        int stevec = 0;
        for (Tekmovalec t : this.tekmovalci) {
            if (t.getPriznanje() == 1) {
                stevec++;
            }
        }
        if (stevec == 0) {
            return "/";
        } else {
            return stevec + "";
        }
    }
}

class Tekmovalec {

    private String id;
    private String ime;
    //0-bronasto,1-zlato,2-srebrno,-1-prazno
    private int priznanje;
    //0-bober,1-bobrcek,2-mladi_bober,3-stari_bober
    private int kategorija;

    public Tekmovalec(String id, String ime, int priznanje, int kategorija) {
        this.id = id;
        this.ime = ime;
        this.priznanje = priznanje;
        this.kategorija = kategorija;
    }

    //Get
    public String getId() {
        return id;
    }

    public String getIme() {
        return ime;
    }

    public int getPriznanje() {
        return priznanje;
    }

    public int getKategorija() {
        return kategorija;
    }

    @Override
    public String toString() {
        return ime;
    }
}