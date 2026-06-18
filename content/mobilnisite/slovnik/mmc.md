---
slug: "mmc"
url: "/mobilnisite/slovnik/mmc/"
type: "slovnik"
title: "MMC – Multimedia Call"
date: 2025-01-01
abbr: "MMC"
fullName: "Multimedia Call"
category: "Services"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/mmc/"
summary: "Multimedia Call (MMC) označuje komunikační službu, která integruje více typů médií, jako je hlas, video a text v reálném čase, v rámci jedné relace volání. Je to klíčový koncept v IMS (IP Multimedia S"
---

MMC je komunikační služba, která integruje více typů médií, jako je hlas, video a text v reálném čase, v rámci jedné relace volání, a umožňuje tak bohaté, interaktivní uživatelské zážitky.

## Popis

Multimedia Call (MMC) je relace zřízená v síti 3GPP, konkrétně prostřednictvím IP Multimedia Subsystem (IMS), která podporuje současnou výměnu více mediálních komponent. Na rozdíl od tradičního hlasového volání v okruhově komutované síti, které je omezeno na jediný audio stream, může MMC dynamicky kombinovat audio, video, text a případně další datové streamy (jako sdílení souborů nebo obrazovky) v rámci jedné koordinované relace. Volání je řízeno pomocí protokolu Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)) pro signalizaci a protokolu Session Description Protocol ([SDP](/mobilnisite/slovnik/sdp/)) pro vyjednání typů médií a používaných kodeků. Mezi klíčové síťové entity patří Proxy-Call Session Control Function ([P-CSCF](/mobilnisite/slovnik/p-cscf/)), Serving-CSCF ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) a Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)) pro případné zpracování nebo mixování médií.

Zřízení MMC začíná SIP INVITE zprávou obsahující SDP nabídku s výčtem typů médií, které volající chce použít. Zařízení příjemce odpoví SDP odpovědí, na které se dohodne společná sada mediálních streamů. Toto vyjednávání umožňuje zařízením s různými schopnostmi najít kompatibilní sadu médií pro volání. Během volání lze další mediální streamy přidávat nebo odebírat pomocí SIP re-INVITE transakcí, což umožňuje funkce jako upgrade hlasového volání na video volání v průběhu relace. Uživatelská rovina pro tyto mediální streamy typicky používá Real-time Transport Protocol ([RTP](/mobilnisite/slovnik/rtp/)) přes IP, směrovaný přímo mezi koncovými body nebo přes mediální brány, pokud je vyžadována spolupráce se staršími sítěmi.

Klíčem pro koncept MMC je role IMS jádra při poskytování servisní logiky, autentizace a řízení politik. S-CSCF aplikuje initial Filter Criteria (iFC) pro spuštění příslušných Application Servers ([AS](/mobilnisite/slovnik/as/)), které mohou pro multimediální volání poskytovat služby s přidanou hodnotou, jako je přesměrování volání na základě stavu dostupnosti nebo interaktivní hlasové/videoodpovědové systémy. Dále Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) interaguje s P-CSCF, aby zajistila, že přenosová síť poskytne vhodnou Quality of Service (QoS) pro na zpoždění citlivé mediální streamy v reálném čase. Tato komplexní koordinace mezi signalizační rovinou (IMS) a transportní rovinou (přístupová a jádrová síť) umožňuje spolehlivý a kvalitní multimediální hovor.

MMC není jedinou službou, ale základní schopností, která umožňuje celou rodinu služeb. Je to podkladový mechanismus pro Videotelefonii, služby Multimedia Telephony (MMTel) a Rich Communication Services (RCS). Správa a účtování těchto komplexních relací jsou zajišťovány specifickými síťovými funkcemi, což je důvod, proč je MMC detailně popsáno v manažerských specifikacích jako TS 32.408. Tato specifikace definuje informační model a procedury pro generování účtovacích dat souvisejících s multimediálními hovory, sledující využití různých mediálních komponent pro účely fakturace.

## K čemu slouží

Multimedia Call byl vytvořen, aby překročil omezení tradiční telefony, která byla navržena výhradně pro obousměrnou hlasovou komunikaci. Jak se sítě vyvíjely směrem k paketově komutovaným IP architekturám s vyšší přenosovou kapacitou, rostla uživatelská poptávka po poutavějších a produktivnějších komunikačních metodách integrujících video a sdílení dat. Účelem MMC je využít rámec IMS k poskytnutí standardizovaného, interoperabilního způsobu zřizování a správy relací obsahujících jakoukoli kombinaci médií v reálném čase, a tím umožnit novou generaci komunikačních služeb.

Historický kontext vychází z oddělení řízení volání a médií ve VoIP systémech a z touhy přinést tuto flexibilitu do mobilních sítí. Předchozí přístupy, jako okruhově komutovaná videotelefonie v 3G sítích (3G-324M), byly rigidní, neefektivní a izolované od internetových služeb. MMC, postavené na IMS, to řeší použitím IP pro signalizaci i média, což umožňuje bezproblémovou integraci s internetovými aplikacemi, dynamické skládání služeb a konvergenci mezi pevnými a mobilními sítěmi. Řeší problém servisních sil tím, že poskytuje jednotný řídicí rámec pro více typů médií.

Navíc MMC umožňuje síťovým operátorům a poskytovatelům třetích stran vytvářet inovativní, zpoplatnitelné služby. Díky standardizovanému modelu toho, co tvoří multimediální hovor, mohou operátoři implementovat sofistikované účtovací modely – například účtovat rozdílně za segmenty pouze s hlasem oproti video segmentům téhož hovoru nebo nabízet balíčky médií. Tato komerční flexibilita, kombinovaná s technickou schopností bohaté interakce, motivovala standardizaci MMC v rámci 3GPP, což z ní učinilo základní kámen moderních IP komunikačních služeb.

## Klíčové vlastnosti

- Podporuje současné, vyjednané mediální streamy (audio, video, text) v rámci jedné SIP relace
- Využívá SIP a SDP pro dynamické zřízení, modifikaci a ukončení relace
- Umožňuje změny modality v průběhu hovoru (např. přidání videa) prostřednictvím procedur SIP re-INVITE
- Integrováno s IMS pro servisní řízení, autentizaci a spouštění aplikací
- Spolupracuje s Policy and Charging Control (PCC) pro vynucení odpovídající QoS na mediálních přenosech
- Generuje podrobné záznamy o účtovacích datech (CDR) pro každou mediální komponentu, jak je definováno v TS 32.408

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MMTEL – Multimedia Telephony Service for IMS](/mobilnisite/slovnik/mmtel/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [P-CSCF – Proxy Call Session Control Function](/mobilnisite/slovnik/p-cscf/)
- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)

## Definující specifikace

- **TS 32.408** (Rel-19) — UMTS/GSM Performance Management Measurements

---

📖 **Anglický originál a plná specifikace:** [MMC na 3GPP Explorer](https://3gpp-explorer.com/glossary/mmc/)
