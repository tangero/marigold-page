---
slug: "nplmn"
url: "/mobilnisite/slovnik/nplmn/"
type: "slovnik"
title: "NPLMN – Number range holder network of the B subscriber"
date: 2025-01-01
abbr: "NPLMN"
fullName: "Number range holder network of the B subscriber"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nplmn/"
summary: "Identifikuje mobilní síť, která drží číselný rozsah (blok MSISDN) pro volaného účastníka (B-účastníka). Používá se při směrování hovorů a účtování, zejména u přenesených čísel, k odlišení původního po"
---

NPLMN je mobilní síť, která původně drží číselný rozsah volaného účastníka; používá se při směrování a účtování k odlišení původního poskytovatele od aktuální obslužné sítě, zejména u přenesených čísel.

## Popis

NPLMN (Number range holder [PLMN](/mobilnisite/slovnik/plmn/)) je specifický typ identifikátoru veřejné pozemní mobilní sítě (PLMN) používaný v telekomunikační logice směrování a účtování. Neidentifikuje síť, ve které účastník aktuálně roamuje nebo je obsluhován; místo toho identifikuje síť, která původně vlastnila nebo jí byl přidělen blok čísel Mobile Subscriber [ISDN](/mobilnisite/slovnik/isdn/) Numbers ([MSISDN](/mobilnisite/slovnik/msisdn/)), do kterého číslo volaného účastníka (B-účastníka) patří. Tento koncept je kriticky důležitý v kontextu přenositelnosti mobilních čísel ([MNP](/mobilnisite/slovnik/mnp/)), kdy může účastník změnit poskytovatele služeb při zachování svého původního telefonního čísla.

Z architektonického hlediska je NPLMN datový prvek uložený v síťových databázích, zejména v databázích přenositelnosti čísel ([NPDB](/mobilnisite/slovnik/npdb/)) nebo jako atribut v Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)). Při volání na přenesené číslo provede Gateway [MSC](/mobilnisite/slovnik/msc/) ([GMSC](/mobilnisite/slovnik/gmsc/)) volající sítě dotaz na přenositelnost čísla. Odpověď obsahuje informace pro směrování (PLMN příjemcovské sítě, RNPLMN) a často i NPLMN pro účely účtování a zúčtování. NPLMN je typicky reprezentován jako Mobile Country Code (MCC) a Mobile Network Code (MNC), stejně jako standardní PLMN ID.

V průběhu hovoru používá GMSC RNPLMN k směrování hovoru do sítě, která aktuálně obsluhuje B-účastníka. NPLMN se však používá při generování záznamů o podrobnostech hovorů (CDR) pro mezifiremní účtování a zúčtování. Protože síť volajícího účastníka může mít různé tarifní dohody s držitelem číselného rozsahu (NPLMN) oproti skutečnému poskytovateli služeb (RNPLMN), je správná identifikace obou nezbytná pro přesné finanční transakce. NPLMN zajišťuje, že výnosy z hovorů na přenesená čísla mohou být vhodně rozděleny mezi operátora, k němuž bylo číslo přeneseno (který poskytuje služby), a operátora-držitele rozsahu (který může poskytovat propojení nebo jiné služby). Jeho role je čistě v administrativní a obchodní vrstvě provozu sítě a zajišťuje správné fungování ekonomického modelu přenositelnosti čísel.

## K čemu slouží

Koncept NPLMN byl vytvořen speciálně k řešení obchodních a provozních výzev, které přinesla přenositelnost mobilních čísel (MNP). Před MNP byl MSISDN účastníka trvale svázán se sítí jeho poskytovatele služeb (HPLMN). Směrování a účtování bylo přímočaré: číselný rozsah MSISDN přímo určoval domovskou síť. MNP toto přímé propojení zrušila, což umožnilo účastníkovi přejít s jeho číslem k jinému operátorovi. To vytvořilo problém: jak má odvětví sledovat, který operátor původně číslo vlastnil, pro účely jako zúčtování poplatků za propojení, účtování a regulatorní reporting?

NPLMN to řeší tím, že trvale spojuje číslo s PLMN, které bylo původně přiděleno tento číselný rozsah národním číslovacím úřadem. To poskytuje pevný, neměnný referenční bod v ekosystému. Bez NPLMN by neexistoval konzistentní způsob, jak určit „původního“ operátora pro přenesené číslo, což by komplikovalo finanční zúčtování a ztěžovalo správu číselných zdrojů. Umožňuje odvětví oddělit koncepty „poskytování služeb“ (řešené RNPLMN) a „vlastnictví/odpovědnost za číselný rozsah“ (řešené NPLMN).

Toto rozlišení je klíčové pro spravedlivou kompenzaci. Poplatky za propojení nebo ukončovací sazby mohou být smluvně dohodnuty na základě identity držitele číselného rozsahu. NPLMN umožňuje přesné generování CDR, aby tyto dohody mohly být dodrženy i po přenesení čísla. Také napomáhá detekci podvodů a regulatornímu dohledu, protože poskytuje trasu zpět k subjektu původně odpovědnému za číslo. V podstatě je NPLMN klíčovým prvkem umožňujícím udržitelný komerční a regulatorní rámec, který činí rozsáhlou přenositelnost čísel proveditelnou.

## Klíčové vlastnosti

- Identifikuje PLMN, který drží původní číselný rozsah MSISDN pro účastníka
- Kritický datový prvek pro provoz v režimu přenositelnosti mobilních čísel (MNP)
- Používá se primárně pro mezifiremní účtování, zúčtování a generování CDR
- Odlišný od PLMN příjemcovské sítě (RNPLMN), který se používá pro směrování hovorů
- Uložen v databázích přenositelnosti čísel (NPDB) a používán v odpovědích na dotazy o přenositelnosti
- Reprezentován jako standardní PLMN ID (MCC+MNC)

## Související pojmy

- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)
- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)
- [MNP – Mobile Number Portability Signalling Relay Function](/mobilnisite/slovnik/mnp/)
- [NPDB – Number Portability Data Base](/mobilnisite/slovnik/npdb/)

## Definující specifikace

- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization

---

📖 **Anglický originál a plná specifikace:** [NPLMN na 3GPP Explorer](https://3gpp-explorer.com/glossary/nplmn/)
