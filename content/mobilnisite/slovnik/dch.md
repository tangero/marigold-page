---
slug: "dch"
url: "/mobilnisite/slovnik/dch/"
type: "slovnik"
title: "DCH – Dedicated Channel"
date: 2025-01-01
abbr: "DCH"
fullName: "Dedicated Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dch/"
summary: "Dedicated Channel (DCH) je transportní kanál v UMTS, který přenáší vyhrazená uživatelská data a řídicí informace mezi UE a RNC. Je mapován na Dedicated Physical Channel (DPCH) a poskytuje bod‑bodové s"
---

DCH je transportní kanál UMTS, který poskytuje vyhrazené, bod‑bodové spojení s proměnnou přenosovou rychlostí pro uživatelská data a řídicí informace mezi UE a RNC a zajišťuje spolehlivou komunikaci.

## Popis

Dedicated Channel (DCH) je klíčový transportní kanál v rádiové přístupové síti UMTS ([UTRAN](/mobilnisite/slovnik/utran/)), definovaný od 3GPP Release 99. Funguje jako obousměrný kanál, zřízený pro každé uživatelské zařízení (UE), aby přenášel vyhrazený provoz, včetně dat uživatelské roviny (např. hlasové rámce, paketová data) a přidružených řídicích informací. DCH je transportní kanál, což znamená, že definuje charakteristiky přenosu dat přes rádiové rozhraní, a je přímo mapován na Dedicated Physical Channel ([DPCH](/mobilnisite/slovnik/dpch/)) ve fyzické vrstvě. Toto mapování zahrnuje procesy jako kanálové kódování, prokládání a přizpůsobování rychlosti, které jsou přizpůsobeny rádiovým podmínkám a požadavkům služby.

Z architektonického hlediska existuje DCH mezi UE a Radio Network Controller ([RNC](/mobilnisite/slovnik/rnc/)). Je zřizován, udržován a uvolňován RNC prostřednictvím signalizace Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) během zřízení nebo rekonfigurace Radio Access Bearer ([RAB](/mobilnisite/slovnik/rab/)). DCH podporuje proměnné přenosové rychlosti, které lze během spojení měnit pomocí výběru Transport Format Combination ([TFC](/mobilnisite/slovnik/tfc/)), což umožňuje dynamické přizpůsobení datovému toku uživatele. Může využívat režim Frequency Division Duplex ([FDD](/mobilnisite/slovnik/fdd/)) nebo Time Division Duplex ([TDD](/mobilnisite/slovnik/tdd/)), přičemž struktura fyzické vrstvy se podle toho liší. V FDD používá DPCH vyhrazené kanalizační a skramblovací kódy k izolaci přenosu uživatele.

Provoz DCH zahrnuje několik klíčových vrstev a protokolů. Na vrstvě Medium Access Control (MAC) jsou data segmentována do transportních bloků a je jim přiřazen Transport Format (TF), který definuje parametry jako velikost bloku a přenosový časový interval (TTI). Pro jedno UE lze multiplexovat více DCH. RNC provádí vnější smyčku řízení výkonu nastavením cílového poměru signálu k šumu (SIR) pro DCH, zatímco rychlá uzavřená smyčka řízení výkonu pracuje na přidruženém DPCH pro potlačení úniků. DCH je ústřední součástí pro služby vyžadující garantovanou kvalitu služeb (QoS), jako je konverzační hlas (kodek AMR) a interaktivní videohovory, protože poskytuje vyhrazené prostředky s řízenou latencí a chybovostí.

Jeho role sahá až k podpoře měkkého předávání, kde může být UE současně připojeno k více Node B přes více DCH, přičemž RNC provádí výběrové kombinování. DCH je těsně integrován s rozhraním lub (mezi Node B a RNC) a rozhraním lu (mezi RNC a Core Network), kde je přenášen v rámci Frame Protocol pro transport uživatelských dat. Ačkoli se jedná primárně o kanál UMTS, jeho koncepty ovlivnily pozdější systémy 3GPP, ačkoli v LTE byly vyhrazené kanály nahrazeny paradigmatem sdíleného kanálu. DCH představuje tradiční model vyhrazených prostředků pro okruhově přepínané a rané paketově přepínané služby v sítích 3G.

## K čemu slouží

DCH byl vytvořen, aby poskytoval vyhrazenou, spolehlivou a kvalitou služeb (QoS) řízenou komunikační cestu pro jednotlivé uživatele v sítích UMTS, čímž řešil omezení struktury kanálů GSM. V GSM byly provozní kanály navrženy primárně pro hlas s konstantní rychlostí, s omezenou flexibilitou pro data. Přechod na 3G si kladl za cíl podporovat širokou škálu služeb s různými požadavky na šířku pásma a kvalitu, od hlasu po video a přístup k internetu. DCH byl klíčovým mechanismem, který to umožnil, tím, že nabídl vyhrazený, obousměrný kanál, který mohl být dynamicky konfigurován z hlediska přenosové rychlosti, kódování a řízení výkonu, přizpůsobený potřebám konkrétní služby.

Řešil problém efektivní podpory jak okruhově přepínaných služeb (jako tradiční telefonie), tak paketově přepínaných služeb (jako prohlížení webu) v rámci jedné rádiové přístupové technologie. Pro okruhově přepínaný hlas poskytoval DCH spojení s konstantní nebo adaptivní přenosovou rychlostí s nízkým zpožděním a řízenou chybovostí, což je zásadní pro hlas ve vysoké kvalitě. Pro paketová data umožňoval proměnné rychlosti a nespojitý přenos, optimalizující využití prostředků při přerušovaném datovém toku. DCH také umožňoval pokročilé rádiové funkce, jako je měkké předávání a rychlé řízení výkonu, které byly klíčové pro zlepšení pokrytí, kapacity a spolehlivosti spojení v sítích UMTS založených na CDMA.

Historicky představoval DCH významný vývoj od sdílených nebo společných kanálů používaných pro počáteční přístup a vysílání. Umožňoval síti přidělit výhradní prostředky uživateli na dobu trvání hovoru nebo relace, čímž zajišťoval izolaci výkonu a předvídatelnou službu. To bylo obzvláště důležité pro aplikace v reálném čase před rozšířením all‑IP architektur a sofistikovaného plánování paketů. Konstrukce DCH odrážela vizi 3GPP o jednotné síti schopné poskytovat multimediální služby, překlenující propast mezi hlasově orientovaným modelem 2G a datově orientovanou budoucností.

## Klíčové vlastnosti

- Bod‑bodový obousměrný transportní kanál vyhrazený pro jedno UE
- Podpora proměnné přenosové rychlosti s dynamickým výběrem Transport Format Combination (TFC)
- Mapování na Dedicated Physical Channel (DPCH) s vyhrazenými kanalizačními a skramblovacími kódy
- Podpora měkkého předávání, umožňující současné připojení k více Node B
- Integrované rychlé uzavřené smyčky řízení výkonu a vnější smyčky řízení výkonu pro adaptaci spojení
- Přenáší jak data uživatelské roviny, tak vyhrazené řídicí informace (např. měřicí hlášení)

## Související pojmy

- [DPCH – Dedicated Physical Channel](/mobilnisite/slovnik/dpch/)
- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.171** (Rel-19) — A-GPS Minimum Performance Requirements for UTRA FDD UE
- **TS 25.201** (Rel-19) — UTRA Physical Layer General Description
- **TS 25.202** (Rel-19) — 7.68Mcps TDD Option Technical Specification
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.225** (Rel-19) — UTRA TDD Physical Layer Measurements
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.303** (Rel-19) — Radio Resource Control Procedures
- … a dalších 28 specifikací

---

📖 **Anglický originál a plná specifikace:** [DCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/dch/)
