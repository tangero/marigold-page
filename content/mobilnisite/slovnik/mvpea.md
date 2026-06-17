---
slug: "mvpea"
url: "/mobilnisite/slovnik/mvpea/"
type: "slovnik"
title: "MVPEA – MCVideo Private Emergency Alert"
date: 2025-01-01
abbr: "MVPEA"
fullName: "MCVideo Private Emergency Alert"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mvpea/"
summary: "MVPEA je služba dle standardu 3GPP, která umožňuje operátorům privátních sítí zasílat cílené nouzové výstrahy uživatelům služby MCVideo (Mission Critical Video). Zajišťuje rychlé a spolehlivé šíření k"
---

MVPEA je služba dle standardu 3GPP, která umožňuje operátorům privátních sítí zasílat cílené nouzové výstrahy uživatelům služby MCVideo, čímž zajišťuje rychlé a spolehlivé šíření kritických informací v rámci profesních skupin, jako jsou jednotky první pomoci.

## Popis

[MCVideo](/mobilnisite/slovnik/mcvideo/) Private Emergency Alert (MVPEA, tj. soukromá nouzová výstraha pro MCVideo) je služba definovaná v rámci architektury služeb kritické komunikace (Mission Critical Services) dle 3GPP, která konkrétně rozšiřuje možnosti služby Mission Critical Video (MCVideo). Funguje jako cílený výstražný mechanismus v rámci privátních či vyhrazených sítí, například těch používaných složkami integrovaného záchranného systému, utility nebo průmyslovými organizacemi. Služba je navržena pro doručování urgentních oznámení, včetně video výstrah, konkrétním jednotlivcům, skupinám nebo všem uživatelům v rámci domény služby MCVideo. Z architektonického hlediska MVPEA využívá stávající architekturu služby MCVideo definovanou v 3GPP TS 24.281, která zahrnuje funkční entity jako MCVideo aplikační server, MCVideo klienty a podkladové jádro IP Multimedia Subsystem (IMS). Výstražný mechanismus je integrován s možnostmi skupinové komunikace a vysílání (broadcast) služby MCVideo.

Operačně může MVPEA výstrahu zahájit autorizovaný uživatel nebo automatizovaný systém. Žádost o výstrahu zpracuje MCVideo aplikační server, který autentizuje původce a určí cílové příjemce na základě předem nakonfigurovaných skupin, rolí nebo individuálních identit. Server poté spustí doručení výstrahy pomocí příslušných protokolů MCVideo pro řízení relace a distribuci médií. Výstrahy lze nastavit jako rušivé, takže přeruší jinou probíhající komunikaci na zařízení uživatele, aby byla zajištěna okamžitá pozornost. Služba obsahuje mechanismy pro potvrzení doručení a pro potvrzení přečtení od příjemců, čímž poskytuje původci výstrahy zpětnou vazbu o jejím dosahu.

Úlohou MVPEA v síti je poskytovat garantovaný, nízkolatenční a zabezpečený kanál pro nouzovou komunikaci v rámci profesního kontextu. Funguje nezávisle na veřejných systémech Commercial Mobile Alert Systems ([CMAS](/mobilnisite/slovnik/cmas/)) nebo Earthquake and Tsunami Warning Systems (ETWS), což umožňuje organizačně specifická upozornění na hrozby, operační pokyny nebo bezpečnostní oznámení. Služba je klíčovou součástí pro zvýšení situačního povědomí a koordinovaného zásahu v rámci operací kritické komunikace, neboť zajišťuje, že kritické informace ve formě videa dorazí k příslušnému personálu bez zbytečného zpoždění.

## K čemu slouží

MVPEA byla vytvořena k řešení potřeby cílené a spolehlivé nouzové komunikace v rámci ekosystémů profesionálních a privátních sítí, zejména pro služby kritické komunikace (Mission Critical). Před její standardizací organizace spoléhaly na méně integrované metody, jako jsou rádiové vysílání, hromadné SMS nebo proprietární aplikace, kterým chybělo garantované doručení, podpora multimédií a integrace s komplety služeb kritické hlasové a video komunikace. Omezení těchto přístupů zahrnovala potenciální zahlcení sítě ovlivňující doručení, absenci potvrzení od uživatele a nemožnost využít správu skupin a mechanismy priority vlastní službám kritické komunikace 3GPP.

Motivace pro MVPEA vycházela ze širší iniciativy 3GPP standardizovat služby kritické komunikace přes sítě LTE a 5G s cílem zajistit interoperabilitu, zabezpečení a funkční paritu s tradičními systémy profesionální mobilní radiokomunikace (PMR). Jak se služba [MCVideo](/mobilnisite/slovnik/mcvideo/) vyvíjela, aby poskytovala video v reálném čase pro složky IZS a průmysl, stala se zjevnou potřeba přidružené výstražné služby. MVPEA řeší problém šíření urgentních vizuálních informací – jako je živé záběry hrozby, evakuační trasy nebo video z místa události – přímo na zařízení zasahujících osob nebo operačního personálu, čímž urychluje rozhodování a reakční časy v rámci kontrolovaného prostředí privátní služby.

## Klíčové vlastnosti

- Cílené doručování výstrah jednotlivcům, předdefinovaným skupinám nebo vysílání (broadcast) všem uživatelům MCVideo
- Podpora výstrah s multimédii včetně video klipů a statických obrázků
- Možnost rušivého zobrazení výstrahy, které může přerušit jiné činnosti na zařízení
- Mechanismy pro potvrzení konečného doručení a přečtení
- Integrace s architekturou služby 3GPP MCVideo a jádrem IMS
- Zabezpečené a autentizované vytvoření a zpracování výstrahy

## Související pojmy

- [MCVideo – Mission Critical Video](/mobilnisite/slovnik/mcvideo/)
- [MCA – MSE Configuration API](/mobilnisite/slovnik/mca/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [CMAS – Commercial Mobile Alert Service](/mobilnisite/slovnik/cmas/)

## Definující specifikace

- **TS 24.281** (Rel-19) — MCVideo Signalling Control Specification
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing

---

📖 **Anglický originál a plná specifikace:** [MVPEA na 3GPP Explorer](https://3gpp-explorer.com/glossary/mvpea/)
