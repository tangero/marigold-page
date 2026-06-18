---
slug: "macs"
url: "/mobilnisite/slovnik/macs/"
type: "slovnik"
title: "MACS – Maximum number of Codecs Modes in the Active Codec Set"
date: 2025-01-01
abbr: "MACS"
fullName: "Maximum number of Codecs Modes in the Active Codec Set"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/macs/"
summary: "MACS definuje maximální počet režimů kodeků, které mohou být současně aktivní v multimediální relaci, jako je videohovor. Jedná se o klíčový parametr pro správu složitosti relace a zajištění toho, aby"
---

MACS (maximální počet režimů kodeků v aktivní sadě kodeků) je maximální počet režimů kodeků, které mohou být současně aktivní v multimediální relaci, což řídí složitost relace za účelem zajištění efektivního využití síťových prostředků a kvality služby.

## Popis

Parametr MACS (Maximum number of Codecs Modes in the Active Codec Set) je definován v rámci specifikací 3GPP pro službu Multimedia Telephony Service for IMS ([MTSI](/mobilnisite/slovnik/mtsi/)) a souvisejících dokumentů. Působí v kontextu vyjednávání a správy relací, zejména pro služby jako je videotelefonie. Aktivní sada kodeků (Active Codec Set, [ACS](/mobilnisite/slovnik/acs/)) označuje soubor režimů kodeků (např. různé datové toky, rozlišení nebo snímkové frekvence pro video kodek jako H.264 nebo H.265), na kterých se dohodnou komunikující koncové body během výměny nabídky/odpovědi protokolu [SDP](/mobilnisite/slovnik/sdp/) (Session Description Protocol). MACS nastavuje horní limit pro velikost této sady.

Z architektonického hlediska je MACS parametrem politiky nebo schopnosti, který ovlivňuje signalizaci protokolů [SIP](/mobilnisite/slovnik/sip/) (Session Initiation Protocol) a SDP. Když koncový bod, jako je uživatelské zařízení (UE) nebo aplikační server, vytvoří SDP nabídku pro multimediální relaci, může uvést více konfigurací kodeku pro daný typ média. Odpovídající koncový bod reaguje SDP odpovědí, ve které vybere nebo přijme podmnožinu těchto možností, čímž vytvoří Aktivní sadu kodeků. Hodnota MACS, kterou lze konfigurovat operátorem sítě nebo která je definována schopnostmi terminálu, omezuje, kolik těchto režimů může být zahrnuto do výsledné, vyjednané ACS. Tím se zabrání vytváření relací s neprakticky velkým počtem současných možností kodeků.

Její role v síti spočívá v vyvážení flexibility a efektivity. Větší ACS umožňuje dynamičtější adaptaci na měnící se síťové podmínky (např. prostřednictvím přepínání režimů kodeku), ale také zvyšuje složitost signalizace, nároky na paměť v koncových bodech a potenciální režii zpracování. Definováním MACS systém zajišťuje, že popisy relací zůstávají zvládnutelné a že koncové body nejsou nuceny podporovat neomezený počet současných stavů kodeků. Je to základní prvek pro předvídatelné chování služby a interoperabilitu mezi zařízeními od různých výrobců, neboť stanovuje společný rámec pro limity složitosti relace.

## K čemu slouží

MACS byl zaveden, aby řešil rostoucí složitost vyjednávání multimediálních relací ve službách založených na IP Multimedia Subsystem (IMS). S rozvojem videotelefonie a pokročilých komunikačních služeb se staly běžnými kodeky podporujícími více režimů (datové toky, profily, úrovně). Bez limitu by teoreticky [SDP](/mobilnisite/slovnik/sdp/) nabídka mohla obsahovat desítky možností kodeků, což by vedlo k několika problémům. Nadměrný počet možností komplikuje proces SDP odpovědi, zvětšuje velikost signalizačních zpráv a vyžaduje vyšší výpočetní výkon koncových bodů pro analýzu a správu všech potenciálních stavů.

Primárním motivem bylo vynutit omezení složitosti popisu relace, aby bylo zajištěno spolehlivé a efektivní navázání relace. Řeší problém potenciálně nekontrolovatelného vyjednávání relace, které by mohlo zhoršit uživatelský zážitek delšími časy sestavování hovoru nebo dokonce způsobit selhání u zařízení s omezenými prostředky. Standardizací MACS poskytlo 3GPP jasný parametr, který umožňuje síťovým operátorům řídit profily relací podle schopností jejich sítě a služebních politik, a tím zajistit konzistentní kvalitu uživatelského zážitku v rámci pokrytí služby. Je to klíčový faktor pro škálovatelné nasazení pokročilých multimediálních služeb přes mobilní sítě.

## Klíčové vlastnosti

- Definuje horní mez pro počet současných režimů kodeků ve vyjednané relaci.
- Použitelné pro multimediální relace v rámci IMS, jako je Multimedia Telephony (MMTel).
- Konfigurovatelný parametr umožňující operátorovi řídit složitost relace.
- Snižuje režii signalizace a nároky na zpracování v koncových bodech.
- Zlepšuje interoperabilitu stanovením společného očekávání pro schopnosti relace.
- Podporuje dynamickou adaptaci tím, že umožňuje řízenou sadu režimů kodeků pro přepínání.

## Související pojmy

- [SDP – Service Discovery Protocol](/mobilnisite/slovnik/sdp/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.153** (Rel-19) — Out-of-Band Transcoder Control Stage 2
- **TS 28.062** (Rel-19) — Tandem Free Operation (TFO) Service Description

---

📖 **Anglický originál a plná specifikace:** [MACS na 3GPP Explorer](https://3gpp-explorer.com/glossary/macs/)
