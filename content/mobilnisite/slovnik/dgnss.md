---
slug: "dgnss"
url: "/mobilnisite/slovnik/dgnss/"
type: "slovnik"
title: "DGNSS – Differential Global Navigation Satellite System"
date: 2025-01-01
abbr: "DGNSS"
fullName: "Differential Global Navigation Satellite System"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dgnss/"
summary: "DGNSS je služba vylepšení polohování, která zvyšuje přesnost GNSS vysíláním korekčních dat přes mobilní sítě. Řeší atmosférické chyby a nepřesnosti satelitních hodin/efemerid, aby poskytla přesnost na"
---

DGNSS je vylepšovací služba, která zvyšuje přesnost Globálního navigačního satelitního systému (GNSS) vysíláním korekčních dat přes mobilní sítě, aby kompenzovala atmosférické nepřesnosti a nepřesnosti satelitů.

## Popis

Differential Global Navigation Satellite System (DGNSS) je polohovací služba definovaná v 3GPP, která vylepšuje přesnost standardních měření Globálního navigačního satelitního systému ([GNSS](/mobilnisite/slovnik/gnss/)) poskytováním korekčních dat mobilním zařízením. Systém funguje porovnáním známých poloh referenčních stanic s měřeními GNSS za účelem výpočtu korekcí chyb, které jsou následně vysílány do uživatelského zařízení (UE) přes mobilní sítě. Tato korekční data kompenzují společné chyby ovlivňující všechny přijímače v dané geografické oblasti, včetně ionosférických a troposférických zpoždění, nepřesností satelitních hodin a chyb orbitálních efemerid.

Architektura zahrnuje referenční stanice na přesně zaměřených lokalitách, které nepřetržitě monitorují signály GNSS z více satelitních konstelací ([GPS](/mobilnisite/slovnik/gps/), [GLONASS](/mobilnisite/slovnik/glonass/), Galileo, BeiDou). Tyto stanice vypočítávají rozdíl mezi svou známou polohou a polohou odvozenou ze surových měření GNSS, čímž generují korekční parametry. Korekční data jsou pak přenášena na DGNSS server, který je formátuje a vysílá do mobilních zařízení přes mobilní infrastrukturu pomocí protokolů pro polohování přes řídicí rovinu nebo uživatelskou rovinu definovaných ve specifikacích 3GPP.

V mobilním zařízení se korekce DGNSS aplikují na surová měření GNSS před výpočtem polohy. UE přijímá asistenční data včetně souřadnic referenčních stanic, korekčních parametrů a informací o platnosti. Zařízení tyto údaje kombinuje s vlastními měřeními GNSS, aby vypočítalo korigovanou polohu s výrazně lepší přesností než při použití samostatného GNSS. Systém podporuje jak korekce v reálném čase pro dynamické aplikace, tak následné zpracování pro aplikace vyžadující přesnost na úrovni geodetického měření.

DGNSS je integrován do polohovací architektury 3GPP prostřednictvím platformy Secure User Plane Location (SUPL) a protokolů pro polohování přes řídicí rovinu. Funguje spolu s dalšími metodami polohování, jako je Assisted GNSS ([A-GNSS](/mobilnisite/slovnik/a-gnss/)), Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)) a Enhanced Cell ID ([E-CID](/mobilnisite/slovnik/e-cid/)), aby poskytoval komplexní polohové služby. Služba je zvláště cenná pro aplikace vyžadující vysokou přesnost, včetně tísňových služeb (E911/E112), vozidlové navigace, geodetického měření a služeb založených na poloze, které potřebují přesnost přesahující možnosti standardního GNSS.

## K čemu slouží

DGNSS byl zaveden, aby řešil omezení přesnosti standardního polohování [GNSS](/mobilnisite/slovnik/gnss/) v mobilních sítích. Zatímco Assisted GNSS ([A-GNSS](/mobilnisite/slovnik/a-gnss/)) zlepšilo čas do prvního fixu a citlivost v indoor/urbánním prostředí, významně nezlepšilo přesnost polohování, která za ideálních podmínek zůstávala na úrovni 5-10 metrů. Mnoho aplikací, zejména tísňové služby, vozidlová navigace a komerční služby založené na poloze, vyžadovalo vyšší přesnost, kterou standardní GNSS nemohl spolehlivě poskytnout kvůli atmosférickým chybám, nepřesnostem satelitních hodin a nejistotám orbitálních efemerid.

Technologie řeší problém společných chyb v měřeních GNSS využitím principu, že přijímače v těsné blízkosti zaznamenávají podobné atmosférické a satelitní chyby. Zřízením referenčních stanic s přesně známými polohami lze tyto společné chyby změřit a vysílat jako korekce do mobilních zařízení. Tento přístup umožňuje přesnost na úrovni centimetrů až metrů bez nutnosti drahých dvoufrekvenčních přijímačů v spotřebitelských zařízeních, čímž činí vysokopřesné polohování ekonomicky proveditelným pro masové aplikace.

3GPP standardizovalo DGNSS, aby vytvořilo interoperabilní rámec pro doručování korekčních dat přes mobilní sítě, a zajistilo tak, že mobilní operátoři mohou nabízet vylepšené polohové služby konzistentně napříč různými sítěmi a zařízeními. Tato standardizace byla zvláště důležitá pro požadavky tísňových služeb (jako E911 v USA a E112 v Evropě), které vyžadovaly stále přesnější informace o poloze, stejně jako pro vznikající aplikace v inteligentních dopravních systémech, precizním zemědělství a rozšířené realitě, které požadovaly přesnost polohování pod úrovní metru.

## Klíčové vlastnosti

- Přenos korekčních dat přes mobilní sítě
- Podpora více konstelací GNSS (GPS, GLONASS, Galileo, BeiDou)
- Integrace s polohovací architekturou 3GPP (SUPL a řídicí rovina)
- Možnosti korekcí v reálném čase a následného zpracování
- Architektura sítě referenčních stanic pro výpočet chyb
- Kompatibilita s existující infrastrukturou A-GNSS

## Související pojmy

- [A-GNSS – Assisted Global Navigation Satellite Systems](/mobilnisite/slovnik/a-gnss/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [E-CID – Enhanced Cell-ID](/mobilnisite/slovnik/e-cid/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)

## Definující specifikace

- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [DGNSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/dgnss/)
