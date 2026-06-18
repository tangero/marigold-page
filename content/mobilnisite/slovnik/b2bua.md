---
slug: "b2bua"
url: "/mobilnisite/slovnik/b2bua/"
type: "slovnik"
title: "B2BUA – Back-to-Back User Agent"
date: 2025-01-01
abbr: "B2BUA"
fullName: "Back-to-Back User Agent"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/b2bua/"
summary: "Síťový prvek založený na SIP, který funguje jako uživatelský agent klient (UAC) i uživatelský agent server (UAS) a zprostředkovává komunikaci mezi dvěma SIP relacemi. Ukončuje a znovu zahajuje signali"
---

B2BUA je síťový prvek SIP, který funguje jako klient i server, aby ukončil a znovu zahájil signalizaci SIP mezi dvěma relacemi, což umožňuje implementaci servisní logiky a řízení v sítích IMS a VoIP.

## Popis

Back-to-Back User Agent (B2BUA) je aplikační server protokolu Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)), který funguje jako prostředník mezi dvěma komunikujícími SIP koncovými body. Na rozdíl od SIP proxy, které pouze přeposílají požadavky, B2BUA ukončuje příchozí SIP dialog od volající strany a navazuje zcela nový odchozí SIP dialog směrem k volané straně. Tím vytváří dvě samostatné SIP relace, které jsou logicky propojeny prostřednictvím servisní logiky B2BUA. B2BUA udržuje plný stav pro obě větve hovoru, včetně identifikátorů dialogů, parametrů relace a informací o médiu, což mu umožňuje vykonávat komplexní kontrolu nad celou komunikační relací.

Architektonicky B2BUA současně implementuje funkce uživatelského agenta klienta ([UAC](/mobilnisite/slovnik/uac/)) i uživatelského agenta serveru ([UAS](/mobilnisite/slovnik/uas/)). Při přijetí požadavku INVITE funguje jako UAS, aby odpověděl původnímu koncovému bodu, a poté okamžitě funguje jako UAC, aby vygeneroval nový požadavek INVITE směrem k cílovému koncovému bodu. Tato architektura s dvojitou rolí umožňuje B2BUA upravovat hlavičky SIP, měnit parametry relace, vkládat nebo odebírat mediální kodeky a manipulovat s nabídkami a odpověďmi [SDP](/mobilnisite/slovnik/sdp/) (Session Description Protocol). B2BUA udržuje samostatné Call-ID, From tagy a To tagy pro každou větev, přičemž je interně koreluje prostřednictvím své aplikační logiky.

V sítích 3GPP jsou B2BUA nasazovány v architektuře IP Multimedia Subsystem (IMS) jako aplikační servery ([AS](/mobilnisite/slovnik/as/)) nebo specializované síťové funkce. Komunikují s funkcí Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) prostřednictvím rozhraní [ISC](/mobilnisite/slovnik/isc/) (IMS Service Control) za použití SIP. B2BUA se může přihlásit k odběru registračních událostí, změn stavu hovoru a dalších SIP událostí od obou koncových bodů, což umožňuje provádění sofistikovaných služeb. Zpracování médií může být buď průchozí (kde média proudí přímo mezi koncovými body), nebo zprostředkované (kde B2BUA obsahuje funkci Media Resource Function pro zpracování).

Klíčové provozní aspekty zahrnují správu stavu relace, korelaci účtování, podporu zákonného odposlechu a spouštění služeb na základě počátečních filtračních kritérií (iFC). B2BUA může implementovat služby jako přesměrování hovorů, hlasovou schránku, předplacené účtování, překlad čísel a systémy interaktivní hlasové odpovědi. Také umožňuje vzájemné propojení mezi různými profily SIP (3GPP IMS SIP versus standardní SIP) a mezi SIP a dalšími signalizačními protokoly prostřednictvím dodatečné funkčnosti brány. Oddělení signalizačních větví umožňuje nezávislé provádění funkcí vůči každému účastníkovi.

## K čemu slouží

B2BUA byla vytvořena, aby řešila základní omezení architektur založených na [SIP](/mobilnisite/slovnik/sip/) proxy při implementaci komplexních telefonních služeb. Jednoduché SIP proxy transparentně přeposílají požadavky bez ukončování dialogů, což omezuje jejich schopnost upravovat relace, vkládat servisní logiku nebo udržovat stav hovoru. Raná nasazení VoIP potřebovala síťové prvky, které by mohly provádět obchodní logiku, aplikovat účtovací politiky a poskytovat služby s přidanou hodnotou podobné tradičním platformám Intelligent Network (IN) v sítích s přepojováním okruhů. Architektura B2BUA tuto schopnost poskytuje plným ukončováním a znovuzahajováním SIP relací.

Historicky koncept B2BUA vznikl z potřeby propojit starší telefonní služby s nově se objevujícími komunikacemi založenými na IP. Když 3GPP vyvíjelo architekturu IMS pro poskytování multimediálních služeb přes paketové sítě, vyžadovalo mechanismus pro implementaci tradičních telefonních funkcí (čekání na hovor, přesměrování, zákazy) a zároveň přidání nových schopností založených na IP. B2BUA poskytla standardizovaný způsob vložení servisní logiky do SIP relací bez nutnosti, aby koncové body podporovaly specifická rozšíření. To bylo obzvláště důležité pro vzájemné propojení různých síťových domén a pro funkce vyžadované regulátory, jako je zákonný odposlech.

Architektura řeší několik kritických problémů: umožňuje poskytovatelům služeb udržovat kontrolu nad relacemi pro účtování a vynucování politik; umožňuje změnu parametrů relace během hovoru; poskytuje bod pro vložení mediálních služeb; a umožňuje interoperabilitu mezi různými implementacemi a verzemi SIP. Bez B2BUA by mnoho pokročilých telefonních služeb vyžadovalo standardizaci komplexních end-to-end mechanismů nebo by je nebylo možné implementovat na síťové straně. Schopnost B2BUA jednat nezávisle vůči každému účastníkovi ji činí nezbytnou pro funkce, které vyžadují asymetrické zacházení s volající a volanou stranou.

## Klíčové vlastnosti

- Úplné ukončení a znovuzahájení SIP dialogu
- Nezávislé řízení relace vůči každému účastníkovi
- Možnosti manipulace s hlavičkami SIP a SDP
- Stavové řízení hovoru s korelací relací
- Vzájemné propojení médií a vyjednávání kodeků
- Integrace s architekturou služeb IMS prostřednictvím rozhraní ISC

## Definující specifikace

- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.719** (Rel-14) — Study on Service Domain Centralization (SeDoC)
- **TS 23.806** (Rel-7) — Voice Call Continuity between CS and IMS
- **TS 23.849** (Rel-11) — Study on IMS Roaming Media Optimization
- **TS 24.182** (Rel-19) — Customized Alerting Tones (CAT) Protocol
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.428** (Rel-7) — Common Basic Communication Procedures
- **TS 24.525** (Rel-19) — Business Trunking Architecture & Requirements
- **TS 24.528** (Rel-8) — Common Basic Communication Procedures for IMS Services
- **TS 24.628** (Rel-19) — Common Basic Communication Procedures in IMS
- **TS 24.802** (Rel-12) — IMS II-NNI Traversal Scenario Determination Study
- **TS 29.079** (Rel-19) — Optimal Media Routeing (OMR) Procedures
- **TS 29.162** (Rel-19) — IMS-IP Network Interworking
- **TS 29.165** (Rel-19) — Inter-IMS Network to Network Interface (NNI)
- **TS 29.421** (Rel-8) — IMS Interworking with External IP Networks
- … a dalších 6 specifikací

---

📖 **Anglický originál a plná specifikace:** [B2BUA na 3GPP Explorer](https://3gpp-explorer.com/glossary/b2bua/)
