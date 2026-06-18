---
slug: "ncp"
url: "/mobilnisite/slovnik/ncp/"
type: "slovnik"
title: "NCP – Network Control Protocol"
date: 2025-01-01
abbr: "NCP"
fullName: "Network Control Protocol"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ncp/"
summary: "Protokol používaný k navázání, udržování a ukončení síťových spojení, zejména v raných systémech 3GPP. Spravuje signalizaci řídicí roviny pro datové relace, zajišťuje správné zřízení a ukončení relace"
---

NCP (Network Control Protocol) je protokol pro řízení sítě používaný v raných systémech 3GPP k navázání, udržování a ukončení síťových spojení prostřednictvím správy signalizace řídicí roviny pro datové relace.

## Popis

Network Control Protocol (NCP) je protokol řídicí roviny definovaný v raných vydáních 3GPP, primárně pro správu kontextů paketového datového protokolu ([PDP](/mobilnisite/slovnik/pdp/)) v sítích [GPRS](/mobilnisite/slovnik/gprs/) a UMTS. Působí mezi mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) a obslužným uzlem podpory GPRS ([SGSN](/mobilnisite/slovnik/sgsn/)) k zřízení, změně a deaktivaci PDP kontextů, které jsou nezbytné pro IP datové relace. Protokol zajišťuje signalizaci pro správu relací, včetně vyjednávání parametrů kvality služby (QoS), přidělování IP adres a správy síťových zdrojů. Je klíčovou součástí vrstvy správy relací GPRS ([SM](/mobilnisite/slovnik/sm/)) a spolupracuje se správou mobility ([MM](/mobilnisite/slovnik/mm/)) k zajištění plynulé datové konektivity.

Z architektonického hlediska je NCP součástí protokolového zásobníku v řídicí rovině, konkrétně v podsložce správy relací. Využívá podpůrná signalizační spojení poskytovaná protokolem řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)) a dalšími protokoly nižších vrstev. Protokol definuje specifické typy zpráv pro aktivaci, deaktivaci a změnu PDP kontextů, z nichž každá obsahuje informační prvky přenášející parametry jako požadovaný profil QoS, název přístupového bodu ([APN](/mobilnisite/slovnik/apn/)) a volby konfigurace protokolu. Tyto zprávy se vyměňují během procedur, jako je aktivace PDP kontextu, kdy MS žádá o datovou relaci a síť odpovídá přidělenými zdroji a adresami.

Během provozu, když uživatel zahájí datovou relaci, MS odešle prostřednictvím NCP do SGSN zprávu Activate PDP Context Request. Tato zpráva obsahuje požadovaný APN a parametry QoS. SGSN následně komunikuje s bránovým uzlem podpory GPRS (GGSN) k vytvoření GTP tunelu a přidělení IP adresy. Po úspěšné alokaci zdrojů odešle SGSN zpět MS zprávu Activate PDP Context Accept, která potvrzuje parametry relace. NCP také zajišťuje změny, jako je přejednání QoS během relace, a deaktivaci při jejím ukončení. Jeho role je klíčová pro efektivní správu zdrojů a zajištění, aby datové relace splňovaly požadovanou úroveň služeb.

Klíčové součásti NCP zahrnují jeho sadu zpráv, stavové automaty pro správu relací a integraci s dalšími síťovými prvky, jako je GGSN a HLR. Protokol podporuje různé typy PDP, včetně IPv4 a IPv6, a komunikuje s funkcemi autentizace a účtování. Ačkoli pozdější vydání vyvinula mechanismy správy relací, NCP položil základy signalizace řídicí roviny v paketově přepínaných sítích a ovlivnil následné protokoly, jako je správa relací EPS (ESM) v LTE a 5G. Jeho návrh klade důraz na spolehlivost a flexibilitu, což umožnilo rané mobilní datové služby.

## K čemu slouží

NCP byl vytvořen, aby poskytl standardizovanou metodu pro správu paketových datových relací v sítích 2.5G a 3G, konkrétně GPRS a UMTS. Před jeho zavedením dominovaly sítě s přepojováním okruhů, kterým chyběly efektivní mechanismy pro dynamickou správu IP relací. NCP vyřešil problém navazování a řízení paketově přepínaných spojení a umožnil mobilní přístup k internetu definováním jasných procedur pro zřízení, změnu a ukončení relace. Řešil potřebu vyjednávání QoS, což sítím umožnilo alokovat zdroje na základě požadavků služby, což bylo klíčové pro rozlišení služeb, jako je prohlížení webu a streamování videa.

Historický kontext vychází z přechodu na paketově přepínaná data na konci 90. let 20. století, kdy mobilní operátoři usilovali o nabídku datových služeb mimo hlas. NCP to umožnil integrací se stávající správou mobility a poskytnutím řídicího protokolu, který dokázal zvládnout složitosti IP relací. Vyřešil omezení dřívějších přístupů, které byly často proprietární nebo nepodporovaly dynamickou správu relací, tím, že nabídl standardizované, interoperabilní řešení. To umožnilo rozsáhlé nasazení mobilních datových služeb a připravilo cestu pro pozdější pokroky v LTE a 5G.

Motivace pro NCP zahrnovaly potřebu efektivního využití síťových zdrojů, podporu více typů PDP a plynulou mobilitu. Definováním protokolu speciálně pro řízení relací zajistilo 3GPP, že sítě mohou škálovat, aby zvládly rostoucí datový provoz při zachování kvality služeb. Role NCP v raných ekosystémech mobilních dat byla zásadní, ovlivnila následné protokoly a přispěla k vývoji mobilního širokopásma.

## Klíčové vlastnosti

- Spravuje aktivaci, změnu a deaktivaci PDP kontextu
- Vyjednává parametry QoS pro datové relace
- Podporuje více typů PDP, včetně IPv4 a IPv6
- Integruje se správou mobility pro plynulé předávání spojení
- Definuje standardizované sady zpráv pro signalizaci řídicí roviny
- Umožňuje interakci mezi MS, SGSN a GGSN

## Související pojmy

- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 27.060** (Rel-19) — TE-MT Interworking for Packet Domain
- **TR 38.808** (Rel-17) — Study on NR above 52.6 GHz to 71 GHz
- **TR 38.812** (Rel-16) — Study on NOMA for NR

---

📖 **Anglický originál a plná specifikace:** [NCP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ncp/)
