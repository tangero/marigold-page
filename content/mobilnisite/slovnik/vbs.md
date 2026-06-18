---
slug: "vbs"
url: "/mobilnisite/slovnik/vbs/"
type: "slovnik"
title: "VBS – Voice Broadcast Service"
date: 2025-01-01
abbr: "VBS"
fullName: "Voice Broadcast Service"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vbs/"
summary: "VBS je skupinová komunikační služba s přepojováním okruhů, která autorizovanému uživateli (dispečerovi) umožňuje současně uskutečnit hlasové volání předem definované skupině účastníků. Je navržena pro"
---

VBS je skupinová komunikační služba s přepojováním okruhů, která autorizovanému dispečerovi umožňuje současně uskutečnit hlasové volání předem definované skupině účastníků pro aplikace s požadavky na vysokou spolehlivost (mission-critical).

## Popis

Služba hlasového vysílání (Voice Broadcast Service, VBS) je standardizovaná 3GPP telefonní služba s přepojováním okruhů umožňující jednosměrnou hlasovou komunikaci (one-to-many). Je základním kamenem raných skupinových komunikačních služeb v sítích GSM a UMTS. Architektura služby je založena na dispečerovi (broadcast talker), který zahájí vysílací hovor předem definované skupině, známé jako oblast vysílacího hovoru (Broadcast Call Area, BCA) neboli skupina. Všichni členové přihlášení k této skupině obdrží oznámení o hovoru a po jeho přijetí jsou připojeni v režimu pouze pro naslouchání k projevu dispečera. Mezi klíčové síťové komponenty patří ústředna mobilní sítě (Mobile Switching Center, [MSC](/mobilnisite/slovnik/msc/)), která obsahuje registr skupinových hovorů (Group Call Register, [GCR](/mobilnisite/slovnik/gcr/)) – databázi ukládající konfiguraci skupin (seznamy členů, oblasti služby). Řadič základnových stanic (Base Station Controller, [BSC](/mobilnisite/slovnik/bsc/) v GSM) nebo řadič rádiové sítě (Radio Network Controller, [RNC](/mobilnisite/slovnik/rnc/) v UMTS) spravuje rádiové zdroje a vytváří vícebodový rádiový kanál (point-to-multipoint) v buňkách, kde se členové skupiny nacházejí.

Služba funguje prostřednictvím definovaného postupu sestavení hovoru. Dispečer pomocí speciálního volacího čísla (Group ID) zahájí vysílací hovor. MSC dotazuje GCR, aby identifikovala členy skupiny a geografickou oblast pro vysílání. Síť následně vyvolá cílové mobilní stanice a vytvoří vyhrazený kanál pro přenos hovoru pro dispečera a sdílené naslouchací kanály pro členy skupiny v příslušných buňkách. Kritickým rysem je arbitráž uplinku: pouze dispečer má právo hovořit; členové skupiny nemohou přenášet hlas zpět ke skupině nebo dispečerovi v rámci stejného hovoru, ačkoli mohou mít samostatný mechanismus pro vyžádání statusu mluvčího. Služba zahrnuje funkce jako přednostní přerušení (pre-emption), kdy mohou být vysílací hovory upřednostněny před běžnými hovory, a aktivaci na základě oblasti, která omezí vysílání na konkrétní buňky.

VBS hraje klíčovou roli v operační koordinaci. Jejím hlavním účelem je rychlé a spolehlivé doručení jednosměrných hlasových pokynů nebo oznámení velké, definované skupině uživatelů. To se zásadně liší od konferenčního hovoru, protože je optimalizována pro jednosměrné šíření s minimálním zpožděním při sestavení a efektivním využitím rádiových zdrojů prostřednictvím sdílených downlink kanálů. Služba je spravována prostřednictvím provizních systémů, kde jsou definovány skupiny a autorizováni členové. VBS byla základní službou pro komunikace ve stylu profesionální mobilní rádiové sítě (Professional Mobile Radio, PMR) přes veřejné buněčné sítě, čímž překlenula propast mezi komerčními buněčnými a tradičními pozemními mobilními rádiovými systémy.

## K čemu slouží

VBS byla vytvořena, aby uspokojila potřebu efektivní skupinové komunikace v rámci veřejných buněčných sítí, konkrétně pro profesionální uživatele a uživatele s požadavky na vysokou spolehlivost (mission-critical). Před její standardizací tito uživatelé spoléhali na uzavřené, dedikované systémy pozemní mobilní rádiové komunikace (land mobile radio, [LMR](/mobilnisite/slovnik/lmr/)), jako jsou [TETRA](/mobilnisite/slovnik/tetra/) nebo [P25](/mobilnisite/slovnik/p25/), které vyžadovaly samostatnou infrastrukturu. Motivací bylo využít všudypřítomné pokrytí a úspory z rozsahu sítí GSM k nabídnutí podobných skupinových hlasových funkcí.

Řešila problém pomalého a z hlediska zdrojů neefektivního vytváření skupin pomocí standardních hlasových hovorů, které by vyžadovaly sestavení více jednotlivých point-to-point spojení. VBS představila síťově orientovaný model správy skupin s rychlým sestavením hovoru k předem definované skupině a optimalizovala využití rádiových zdrojů prostřednictvím vícebodových spojení (point-to-multipoint) na downlinku. Tím byly řešeny limity pro aplikace, jako je velení a řízení v oblasti veřejné bezpečnosti, kde velitel potřebuje okamžitě oslovit všechny jednotky v sektoru, nebo pro dopravní dispečery komunikující se všemi řidiči ve vozovém parku.

Historicky byla VBS součástí širšího souboru funkcí služby skupinového hlasového volání (Voice Group Call Service, [VGCS](/mobilnisite/slovnik/vgcs/)) představeného v 3GPP Release 4, který se vyvinul z dřívějších specifikací GSM Phase 2+. Poskytla standardizovanou, interoperabilní alternativu k proprietárním řešením dodavatelů. Ačkoli byla později z hlediska důrazu nahrazena IP službou Mission Critical Push-To-Talk (MCPTT) v LTE a 5G, VBS zůstává nasazenou a spolehlivou službou v mnoha 2G a 3G sítích po celém světě a slouží jako technologický předchůdce moderních širokopásmových skupinových komunikačních služeb.

## Klíčové vlastnosti

- Hlasové volání typu jeden-vůči-mnoha (one-to-many) s uplinkem řízeným dispečerem
- Předem definované statické nebo dynamické členství ve skupině (oblast vysílacího hovoru – Broadcast Call Area)
- Rychlé sestavení hovoru pomocí volání skupinového identifikátoru (Group ID)
- Efektivní využití sdílených rádiových zdrojů na downlinku v cílových buňkách
- Síťově orientované řízení s registrem skupinových hovorů (Group Call Register, GCR) v MSC
- Podpora priority a přednostního přerušení (pre-emption) oproti běžným buněčným hovorům

## Související pojmy

- [VGCS – Voice Group Call Service](/mobilnisite/slovnik/vgcs/)
- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)
- [GCR – Global Call Reference](/mobilnisite/slovnik/gcr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.067** (Rel-19) — Enhanced Multi-Level Precedence and Pre-emption Service
- **TS 23.110** (Rel-19) — Access Stratum Services Specification
- **TS 23.796** (Rel-16) — FRMCS Architectural Analysis
- **TS 24.067** (Rel-19) — eMLPP Supplementary Service Procedures
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TS 27.007** (Rel-19) — AT Command Set for UE
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 43.020** (Rel-19) — Security Procedures for GSM
- **TS 43.068** (Rel-19) — Voice Group Call Service (VGCS) Stage 2
- **TS 43.069** (Rel-19) — Voice Broadcast Service (VBS) Stage 2
- **TR 43.901** (Rel-19) — Generic Access to A/Gb Interface Feasibility Study
- **TS 55.236** (Rel-19) — A8_V MILENAGE Algorithm for VGCS/VBS Security

---

📖 **Anglický originál a plná specifikace:** [VBS na 3GPP Explorer](https://3gpp-explorer.com/glossary/vbs/)
