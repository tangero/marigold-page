---
slug: "adr"
url: "/mobilnisite/slovnik/adr/"
type: "slovnik"
title: "ADR – Accumulated Delta-Range"
date: 2025-01-01
abbr: "ADR"
fullName: "Accumulated Delta-Range"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/adr/"
summary: "Accumulated Delta-Range (ADR) je metoda určování polohy v sítích 3GPP, která využívá měření fáze nosné vlny ze satelitů GNSS k dosažení vysoké přesnosti určení polohy, často až na centimetrové úrovni."
---

ADR je vysoce přesná metoda určování polohy podle 3GPP, která využívá měření fáze nosné vlny GNSS k dosažení přesnosti na úrovni centimetrů pro aplikace jako autonomní vozidla nebo geodetické práce.

## Popis

Accumulated Delta-Range (ADR) je sofistikovaná metoda určování polohy definovaná ve standardech 3GPP, která primárně využívá signály globálních navigačních satelitních systémů ([GNSS](/mobilnisite/slovnik/gnss/)), jako jsou [GPS](/mobilnisite/slovnik/gps/), Galileo nebo BeiDou. Na rozdíl od základního určování polohy založeného na pseudovzdálenosti, které měří dobu letu signálu, se ADR zaměřuje na fázi nosné vlny rádiového signálu vysílaného satelity. Fáze nosné vlny poskytuje mnohem jemnější rozlišení měření, protože vlnová délka nosného signálu (např. pásmo [L1](/mobilnisite/slovnik/l1/) u GPS cca 19 cm) je výrazně kratší než délka čipu pseudonáhodného šumu (PRN) používaného ve standardním určování polohy. ADR měří akumulovanou změnu fáze nosného signálu v čase, čímž efektivně sleduje delta-vzdálenost (změnu vzdálenosti) mezi přijímačem a satelitem s extrémní přesností. Tento proces zahrnuje kontinuální integraci fázových měření, která dokážou detekovat pohyby malé jako zlomek vlnové délky nosné vlny.

Architektura pro určování polohy pomocí ADR zahrnuje několik klíčových komponent: uživatelské zařízení (UE) vybavené přijímačem GNSS schopným sledování fáze nosné vlny, konstelaci satelitů GNSS a často také síťový asistenční prvek, jako je Location Server (např. Enhanced Serving Mobile Location Centre, [E-SMLC](/mobilnisite/slovnik/e-smlc/)) nebo platforma Secure User Plane Location (SUPL). UE měří fázi nosné vlny z více satelitů současně. Nezpracovaná měření fáze nosné vlny jsou však nejednoznačná kvůli celočíselnému počtu celých vlnových délek mezi satelitem a přijímačem – tomu se říká problém celočíselné nejednoznačnosti. K jejímu vyřešení a dosažení absolutní polohy ADR často používá diferenciální techniky, jako je Real-Time Kinematic (RTK) nebo Precise Point Positioning (PPP), které využívají korekce z referenčních stanic nebo satelitních augmentačních systémů ke zmírnění chyb způsobených ionosférickým zpožděním, troposférickým zpožděním a odchylkami satelitních hodin.

Během provozu UE nebo síťová entita akumuluje měření delta-vzdálenosti v čase, čímž vytváří přesnou historii relativního pohybu. Kombinací ADR měření ze čtyř nebo více satelitů a vyřešením celočíselných nejednoznačností může systém vypočítat vysoce přesnou trojrozměrnou polohu. V rámci 3GPP je ADR integrována do protokolů pro určování polohy v řídicí rovině a uživatelské rovině, specifikovaných v dokumentech jako TS 36.355 (LTE Positioning Protocol, [LPP](/mobilnisite/slovnik/lpp/)) a TS 37.355 (LTE Positioning Protocol Annex, LPPa). Location Server může asistovat UE poskytováním efemeridních dat, ionosférických modelů nebo diferenciálních korekcí pro zvýšení přesnosti a zkrácení doby do prvního určení polohy (TTFF). Role ADR je zvláště důležitá v sítích LTE (od Release 8 dále) a 5G NR, kde podporuje pokročilé služby založené na poloze ([LBS](/mobilnisite/slovnik/lbs/)), nouzové služby jako E911 s požadavky na zvýšenou přesnost a nové případy užití, jako je komunikace Vehicle-to-Everything (V2X) a navigace dronů.

Technická implementace zahrnuje sofistikované zpracování signálu v přijímači GNSS v UE, včetně smyček fázového závěsu (PLL) pro sledování fáze nosné vlny a zvládání dynamiky, jako je Dopplerův jev. Měření jsou typicky reportována v podobě akumulovaných cyklů fáze nosné vlny, často s měřítkovým faktorem. Data ADR spolu s dalšími měřeními, jako je pseudovzdálenost a Dopplerův jev, jsou zabalena do zpráv pro určení polohy (např. LPP Provide Location Information) odesílaných do sítě. V 5G se rámec podle TS 38.305 rozšiřuje na NG-RAN a podporuje podobné služby vysoce přesného určování polohy. ADR umožňuje nejen statické určení polohy, ale také přesné stanovení rychlosti a orientace analýzou rychlosti změny fáze a rozdílů mezi více anténami, což je klíčové pro aplikace jako autonomní řízení a precizní zemědělství.

## K čemu slouží

ADR bylo zavedeno jako odpověď na rostoucí poptávku po vysoce přesném určování polohy přesahujícím možnosti tradičních metod [GNSS](/mobilnisite/slovnik/gnss/), jako je standardní polohová služba (SPS) založená na měření pseudovzdálenosti. Předchozí techniky, omezené rozlišením kódové fáze (přesnost na úrovni metrů kvůli hrubé rychlosti změny PRN kódu), byly nedostatečné pro nově vznikající aplikace, jako je geofencing, rozšířená realita a inteligentní dopravní systémy. Motivace vycházela z komerčních, bezpečnostních a regulatorních potřeb; například požadavky na rozšířenou službu 911 (E911) v některých regionech začaly vyžadovat přesnější určení polohy pro záchranné složky, zatímco odvětví jako stavebnictví a logistika požadovala centimetrovou přesnost pro sledování majetku a automatizaci.

Historicky bylo vysoce přesné určování polohy omezeno na specializované geodetické vybavení používající drahé, samostatné systémy RTK. Standardizace ADR v 3GPP, počínaje Release 8 pro LTE, si kladla za cíl demokratizovat tuto technologii jejím integrováním do běžných mobilních zařízení a síťové infrastruktury. Tato integrace umožňuje UE využívat síťovou asistenci – například diferenciální korekce doručované přes mobilní spojení – k rychlejšímu a spolehlivějšímu řešení nejednoznačnosti fáze nosné vlny, čímž se překonávají omezení jako dlouhá doba konvergence a potřeba vyhrazených základnových stanic. Vložením ADR do standardů mobilních sítí umožnilo 3GPP zařízením masového trhu dosáhnout přesnosti na úrovni decimetrů nebo centimetrů bez nutnosti externího proprietárního hardwaru, a tím podpořilo inovace v službách využívajících polohu.

ADR navíc řeší kritické problémy v městském a náročném prostředí, kde jsou satelitní signály zeslabovány nebo odráženy (vícecestné šíření). Zatímco základní GNSS v takových scénářích selhává, měření fáze nosné vlny ADR, kombinovaná s fúzí senzorů (např. inerciálními měřicími jednotkami) a síťovou hybridizací, poskytuje robustní kontinuitu určování polohy. Tato schopnost je klíčová pro autonomní vozidla navigující v komplexním městském prostředí nebo drony provádějící přesné manévry. Shrnutím, ADR existuje proto, aby překlenulo propast mezi běžným určováním polohy a přesností na úrovni geodetických přístrojů, čímž otevírá nové vertikály a vylepšuje stávající služby prostřednictvím vyšší přesnosti, spolehlivosti a integrace s mobilními sítěmi.

## Klíčové vlastnosti

- Měření fáze nosné vlny pro přesnost na úrovni pod centimetr
- Síťem asistované řešení celočíselné nejednoznačnosti pomocí protokolů jako LPP
- Podpora diferenciálních technik (RTK, PPP) pro zmírnění chyb
- Integrace s rámci pro určování polohy v řídicí rovině (LPP) a uživatelské rovině (SUPL) podle 3GPP
- Kompatibilita s více konstelacemi GNSS (GPS, Galileo, BeiDou, GLONASS)
- Umožňuje sledování mobility s vysokou přesností pro dynamické aplikace jako V2X

## Související pojmy

- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [E-SMLC – Enhanced Serving Mobile Location Centre](/mobilnisite/slovnik/e-smlc/)
- [GNSS – Global Navigation Satellite System](/mobilnisite/slovnik/gnss/)

## Definující specifikace

- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2
- **TS 44.031** (Rel-19) — Radio Resource LCS Protocol (RRLP)

---

📖 **Anglický originál a plná specifikace:** [ADR na 3GPP Explorer](https://3gpp-explorer.com/glossary/adr/)
