---
slug: "mhi"
url: "/mobilnisite/slovnik/mhi/"
type: "slovnik"
title: "MHI – Mobility History Information"
date: 2026-01-01
abbr: "MHI"
fullName: "Mobility History Information"
category: "Mobility"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/mhi/"
summary: "MHI je datový záznam obsahující minulé pohybové vzorce uživatelského zařízení (UE), například předchozí asociace s buňkami a historii předávání hovoru. Síť jej používá k predikci budoucí mobility, což"
---

MHI je datový záznam obsahující minulé pohybové vzorce uživatelského zařízení (UE), jako například předchozí asociace s buňkami, který síť využívá k predikci budoucí mobility za účelem efektivnějších rozhodnutí o předávání hovoru a optimalizace.

## Popis

Mobility History Information (MHI) je strukturovaný soubor dat generovaný a udržovaný uživatelským zařízením (UE) a/nebo sítí, který podrobně popisuje historické pohybové chování UE. Tyto informace jsou primárně definovány v kontextu protokolu řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)) v 5G New Radio (NR). UE typicky zaznamenává klíčové pohybové události, jako jsou úspěšná předání hovoru, obnovení spojení a převýběry buněk, spolu s přidruženými parametry, jako jsou identity zdrojové a cílové buňky, časová razítka a rádiové podmínky v době události. Tento záznam tvoří záznam MHI.

Síť, konkrétně Next Generation NodeB (gNB), může tyto informace vyžádat od UE prostřednictvím signalizace RRC, například během procedury UE Information Request. Po přijetí žádosti UE poskytne hlášení MHI. Funkce řízení rádiových zdrojů ([RRM](/mobilnisite/slovnik/rrm/)) gNB následně tato historická data zpracují. Analýzou vzorců – jako jsou častá předání hovoru mezi konkrétními buňkami, typické trajektorie pohybu nebo oblasti náchylné k selháním – mohou algoritmy RRM vytvořit prediktivní model mobility UE.

Tato prediktivní schopnost je klíčová pro fungování MHI. Například, pokud historie UE ukazuje, že se konzistentně pohybuje z buňky A do buňky B po krátkém pobytu v buňce A, obsluhující gNB může proaktivně připravit zdroje v buňce B nebo dokonce zahájit podmíněné předání hovoru dříve a spolehlivěji. Tím se snižuje míra selhání předání hovoru a doba přerušení. Dále MHI napomáhá optimalizacím zaměřeným na síť. Systémy správy sítě ([NMS](/mobilnisite/slovnik/nms/)) nebo samotný gNB mohou agregovat hlášení MHI od více uživatelských zařízení, aby identifikovaly systémové problémy, jako jsou díry v pokrytí buněk, oblasti s trvalým rušením nebo nevyvážené zatížení provozu mezi sousedními buňkami, což vede k nápravným změnám konfigurace.

Specifikace upravující MHI, jako je 3GPP TS 38.306 (rádiové přístupové schopnosti UE) a série 28.622/32.42x (řízení), definují informační prvky, procedury hlášení a aspekty řízení. MHI vylepšuje tradiční správu mobility založenou na okamžitých měřeních přidáním časového rozměru, což síti umožňuje činit rozhodnutí na základě naučeného chování, nikoli pouze na momentálním snímku aktuálních rádiových podmínek.

## K čemu slouží

MHI bylo zavedeno, aby řešilo výzvy správy mobility v stále hustších a heterogenních sítích 5G a novějších generací. Tradiční rozhodování o předání hovoru se silně opírá o hlášení měření v reálném čase (např. Reference Signal Received Power - [RSRP](/mobilnisite/slovnik/rsrp/)). Ačkoli je tento přístup účinný, může v situacích s vysokou rychlostí, ultra-hustými nasazeními a složitými prostředími s více paprsky selhávat, což vede k pozdním, neúspěšným nebo zbytečným předáním hovoru (ping-pong efekt). Tato selhání zhoršují uživatelský zážitek a spotřebovávají zbytečné signalizační prostředky.

Základní problém, který MHI řeší, je nedostatek kontextu v rozhodnutích o mobilitě. Poskytnutím historie pohybů UE získává síť prediktivní vhled. To umožňuje proaktivnější a inteligentnější správu zdrojů. Například umožňuje prediktivní předání hovoru, kdy je cílová buňka připravena předem na základě trajektorie UE, což výrazně snižuje riziko selhání předání hovoru a přerušení dat. To je klíčové pro zajištění bezproblémové mobility pro případy použití, jako jsou vozidlové komunikace ([V2X](/mobilnisite/slovnik/v2x/)) a vysokorychlostní vlaky.

Dále MHI podporuje pokročilé funkce automatizace sítě a samo-organizujících sítí ([SON](/mobilnisite/slovnik/son/)). Shromažďováním pohybových historií z populace uživatelských zařízení mohou operátoři provádět daty řízenou optimalizaci hranic buněk (optimalizace robustnosti mobility), sklonů antén a parametrů předání hovoru. Tím se ladění sítě posouvá z reaktivního, manuálního procesu na proaktivní, daty řízený proces, což zlepšuje celkovou efektivitu a stabilitu sítě. Jeho specifikace napříč standardy pro rádiový přístup (38-série) i řízení (28/32-série) podtrhuje jeho roli klíčového enableru pro inteligentní, automatizované systémy 5G.

## Klíčové vlastnosti

- Zaznamenává historické pohybové události UE (předání hovoru, převýběry buněk)
- Lze nahlásit od UE k gNB prostřednictvím signalizace RRC na žádost sítě
- Umožňuje prediktivní správu mobility a předání hovoru
- Podporuje optimalizaci robustnosti mobility (MRO) a vyrovnávání zatížení
- Poskytuje vstup pro síťovou analytiku a funkce SON
- Definováno pro 5G NR s zpětně kompatibilními rozhraními pro řízení

## Definující specifikace

- **TS 28.622** (Rel-20) — Telecommunication Management; Generic NRM Information Service
- **TS 32.421** (Rel-19) — Subscriber & Equipment Trace Concepts & Requirements
- **TS 32.422** (Rel-20) — Telecom Management: Trace Control & Configuration
- **TS 38.306** (Rel-19) — NR UE Radio Access Capability Parameters

---

📖 **Anglický originál a plná specifikace:** [MHI na 3GPP Explorer](https://3gpp-explorer.com/glossary/mhi/)
