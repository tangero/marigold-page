---
slug: "vbc"
url: "/mobilnisite/slovnik/vbc/"
type: "slovnik"
title: "VBC – Volume Based Charging"
date: 2025-01-01
abbr: "VBC"
fullName: "Volume Based Charging"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/vbc/"
summary: "Volume Based Charging (VBC, účtování podle objemu) je mechanismus účtování dle 3GPP, který vypočítává náklady na službu na základě celkového objemu dat spotřebovaných uživatelem, nikoli na základě dob"
---

VBC je mechanismus účtování dle 3GPP, který vypočítává náklady na službu na základě celkového objemu dat spotřebovaných uživatelem, což umožňuje flexibilní fakturační modely, jako jsou stupňované datové tarify.

## Popis

Volume Based Charging (VBC, účtování podle objemu) je standardizovaná funkce online systému účtování ([OCS](/mobilnisite/slovnik/ocs/)) v rámci architektury 3GPP, specifikovaná primárně v TS 24.147. Funguje tak, že monitoruje a měří množství dat (v bajtech) přenesených během datové relace uživatele, jako je kontext [PDP](/mobilnisite/slovnik/pdp/) (Packet Data Protocol) v 4G nebo [PDU](/mobilnisite/slovnik/pdu/) Session v 5G. Tento účtovací mechanismus je integrován s prvky jádra sítě, jako je Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) ve 4G nebo Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) v 5G, které vynucují zásady, a s Charging Data Function ([CDF](/mobilnisite/slovnik/cdf/)) nebo Online Charging System (OCS), které shromažďují záznamy o účtovacích datech ([CDR](/mobilnisite/slovnik/cdr/)) nebo provádějí řízení kreditu v reálném čase. Když uživatel zahájí datovou relaci, síť spustí účtovací relaci, ve které serving gateway ([SGW](/mobilnisite/slovnik/sgw/)) nebo user plane function (UPF) hlásí objemy datového využití účtovacímu systému v nastavených intervalech nebo při dosažení prahových hodnot. OCS poté odečte kredit z účtu uživatele na základě nahlášeného objemu, případně s uplatněním různých tarifních sazeb v závislosti na službě, denní době nebo stavu sítě. Tento proces umožňuje správu kvót v reálném čase, kdy síť může přidělit konkrétní kvótu objemu dat a po jejím vyčerpání na základě politiky operátora požádat o novou kvótu nebo relaci ukončit/omezit. VBC je základním kamenem moderního zpoplatnění datových služeb, který umožňuje přesné a detailní účtování odpovídající skutečné spotřebě prostředků.

## K čemu slouží

Volume Based Charging (účtování podle objemu) bylo vytvořeno, aby řešilo omezení tradičních modelů účtování, jako je účtování podle délky (běžné u hlasových hovorů) nebo paušální účtování, které nebyly vhodné pro přerušované, paketově přepínané datové služby. Jak se mobilní sítě vyvíjely od okruhově přepínaného hlasu k paketově přepínaným datům (GPRS, 3G, 4G, 5G), využívání dat se stalo velmi proměnlivým, což činilo časové účtování nespravedlivým a paušální sazby pro operátory neudržitelnými kvůli nepředvídatelnému zatížení sítě. VBC poskytuje spravedlivou a přesnou metodu, jak uživatelům účtovat přesně za množství dat, které spotřebují, což je zásadní pro komerční úspěch mobilního širokopásmového připojení. Umožňuje operátorům nabízet flexibilní tarifní plány, jako je platba za využití, stupňované datové balíčky a sdílené datové plány, které vyhovují různým potřebám uživatelů a vzorcům spotřeby. Historicky jeho zavedení podpořilo přechod od hlasově orientovaných k datově orientovaným výnosovým modelům, což operátorům umožnilo efektivně spravovat síťové prostředky a zároveň poskytovat zákazníkům transparentnost. Bez VBC by bylo výrazně obtížnější zavádět složité datové plány, politiky spravedlivého využívání a kontroly výdajů v reálném čase.

## Klíčové vlastnosti

- Účtování na základě naměřeného objemu dat (vstupní, výstupní nebo celkový)
- Řízení kreditu a správa kvót v reálném čase prostřednictvím OCS
- Integrace s řízením zásad (PCRF/PCF) pro účtování s ohledem na službu
- Podpora různých tarifních sazeb uplatňovaných na konkrétní datové toky nebo služby
- Generování podrobných záznamů o účtovacích datech (CDR) pro fakturaci
- Schopnost spouštět oznámení nebo akce po vyčerpání kvóty

## Související pojmy

- [OCS – Originating Call Screening](/mobilnisite/slovnik/ocs/)
- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)
- [CDR – Call Detail Record](/mobilnisite/slovnik/cdr/)

## Definující specifikace

- **TS 24.147** (Rel-19) — IMS Conferencing Protocol Details

---

📖 **Anglický originál a plná specifikace:** [VBC na 3GPP Explorer](https://3gpp-explorer.com/glossary/vbc/)
