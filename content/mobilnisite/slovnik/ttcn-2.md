---
slug: "ttcn-2"
url: "/mobilnisite/slovnik/ttcn-2/"
type: "slovnik"
title: "TTCN-2 – Tree and Tabular Combined Notation version 2"
date: 2025-01-01
abbr: "TTCN-2"
fullName: "Tree and Tabular Combined Notation version 2"
category: "Protocol"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/ttcn-2/"
summary: "TTCN-2 je druhá hlavní verze testovacího jazyka TTCN, která zachovává původní tabulkový formát, ale s významnými vylepšeními ve strukturování a vyjadřovacích schopnostech. Byla použita pro většinu tes"
---

TTCN-2 je druhá verze testovacího jazyka Tree and Tabular Combined Notation, která se vyznačuje vylepšenou strukturou a je rozsáhle používána pro testování shody (conformance testing) v mobilních sítích 3G a 4G podle specifikací 3GPP.

## Popis

TTCN-2 představuje zralou, široce nasazenou verzi jazyka Tree and Tabular Combined Notation, která navázala na původní [TTCN](/mobilnisite/slovnik/ttcn/) (někdy zpětně označovanou jako TTCN-1). Je to verze odkazovaná ve všech vydáních 3GPP až včetně LTE. TTCN-2 si zachovává základní paradigma abstraktní, deklarativní specifikace testů, ale oproti svému předchůdci zavedla formalizovanější strukturální koncepty a rozšířené možnosti. Testovací sada TTCN-2 je organizována do několika tabulkových sekcí: Tabulka deklarací (pro datové typy, konstanty a parametry testovací sady), Tabulka omezení (definující konkrétní instance zpráv a signálů s detailními hodnotami polí), Tabulka dynamického chování (jádro popisující chování testovacího případu jako sekvence odesílání, přijímání a rozhodovacích bodů) a Tabulka alokace testovacích případů.

Fungování TTCN-2 zahrnuje jasné oddělení mezi abstraktní testovací sadou ([ATS](/mobilnisite/slovnik/ats/)), napsanou v TTCN-2, a spustitelnou testovací sadou ([ETS](/mobilnisite/slovnik/ets/)), která běží na testovací platformě. ATS definuje *co* testovat. Kompilátor přeloží tabulky TTCN-2 do mezikódu. Tento kód je pak vykonáván běhovým systémem TTCN-2, který spoléhá na Adaptér platformy ([PA](/mobilnisite/slovnik/pa/)) a Rozhraní kodéru ([CI](/mobilnisite/slovnik/ci/)) pro zvládnutí konkrétních, systémově specifických úloh. PA spravuje časovače, externí funkce a komunikaci s fyzickým rozhraním testovaného systému ([SUT](/mobilnisite/slovnik/sut/)). CI je zodpovědný za konkrétní kódování abstraktních [PDU](/mobilnisite/slovnik/pdu/) do bitových řetězců (např. ASN.1 [PER](/mobilnisite/slovnik/per/) kódování pro protokoly 3GPP) a naopak. Tato architektura zajišťuje, že samotná testovací logika zůstává přenositelná a znovupoužitelná na různých testovacích platformách a rozhraních SUT.

Mezi klíčové architektonické komponenty TTCN-2 patří koncept Testovacích komponent (MTC - Hlavní testovací komponenta a PTCs - Paralelní testovací komponenty), které umožňují testování distribuovaných systémů s více spojeními. Podporuje výkonné mechanismy porovnávání šablon pro přijaté zprávy, včetně použití symbolů 'ANY' nebo 'OMIT' pro ignorování určitých polí. Jazyk také obsahuje konstrukce pro cykly, gotos (ačkoli používané střídmě) a přiřazování testovacích verdiktů. V rámci 3GPP bylo TTCN-2 použito k vytvoření rozsáhlých, komplexních testovacích sad pro protokoly jako RRC, MAC, RLC, NAS a signalizaci IMS (SIP). Tyto sady jsou často tisíce stránek dlouhé ve své tabulkové podobě a jsou základem pro všechna testování shody prováděná akreditovanými laboratořemi.

## K čemu slouží

TTCN-2 byla vyvinuta, aby odstranila omezení původního TTCN, a poskytla robustnější, strukturovanější a funkčně bohatší jazyk schopný zvládnout explodující složitost protokolů 3G (UMTS) a později 4G (LTE). Původní TTCN měla méně formalizovaná pravidla pro strukturování a méně konstrukcí pro správu velkých testovacích sad. TTCN-2 zavedla lepší modularitu, jasnější pravidla pro rozsah platnosti a vylepšenou podporu definic datových typů (v souladu s ASN.1), což bylo klíčové pro protokoly 3GPP intenzivně využívající ASN.1.

Jejím účelem zůstalo jednoznačně umožnění důkladného, standardizovaného testování shody. Jak se systémy 3GPP staly globálním standardem pro mobilní komunikaci, ekonomické důsledky interoperability prudce vzrostly. TTCN-2 poskytla potřebnou přesnost a škálovatelnost pro vytváření testovacích sad, které mohly důkladně prověřit množství povinných a volitelných funkcí definovaných ve stovkách technických specifikací. Umožnila tvůrcům testů vytvářet složité scénáře zahrnující více paralelních procedur (např. hlasový hovor při provádění předání spojení a aktivaci PDP kontextu na pozadí), což bylo zásadní pro prokázání robustnosti v reálném provozu.

Dlouhověkost TTCN-2 až do vydání 3GPP 14 a její použití v testovacích sadách pro LTE je důkazem jejího úspěchu. Sloužila jako pracovní jazyk pro certifikaci mobilních technologií po více než desetiletí. Motivací pro následný vývoj směrem k TTCN-3 (od vydání 15 pro 5G) byla snaha o modernější, textovou syntaxi a lepší integraci s nástroji softwarového inženýrství, ale TTCN-2 splnila svůj účel zajištění interoperability miliard zařízení 3G a 4G po celém světě.

## Klíčové vlastnosti

- Vylepšený, standardizovaný tabulkový formát pro strukturu testovací sady (tabulky deklarací, omezení, dynamického chování).
- Formalizovaná podpora datových typů Abstract Syntax Notation One (ASN.1) hojně používaných v 3GPP.
- Zavedení strukturovaných testovacích komponent (MTC, PTCs) pro modelování souběžných procesů.
- Výkonný systém šablon a omezení pro definování obsahu očekávaných a odesílaných zpráv.
- Jasná prováděcí architektura oddělující Abstraktní testovací sadu od Adaptéru platformy a Kodéru.
- Definitivní jazyk pro specifikace testů shody protokolů 3G (UMTS) a 4G (LTE).

## Související pojmy

- [TTCN-3 – Testing and Test Control Notation version 3](/mobilnisite/slovnik/ttcn-3/)

## Definující specifikace

- **TR 21.801** (Rel-19) — 3GPP Specification Drafting Rules
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [TTCN-2 na 3GPP Explorer](https://3gpp-explorer.com/glossary/ttcn-2/)
