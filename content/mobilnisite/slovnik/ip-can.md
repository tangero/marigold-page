---
slug: "ip-can"
url: "/mobilnisite/slovnik/ip-can/"
type: "slovnik"
title: "IP-CAN – IP-Connectivity Access Network"
date: 2025-01-01
abbr: "IP-CAN"
fullName: "IP-Connectivity Access Network"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ip-can/"
summary: "Konceptuální síť, která poskytuje IP konektivitu mezi uživatelským zařízením (UE) a externí IP sítí, jako je internet nebo IMS. Je základem pro umožnění všech služeb založených na IP v systémech 3GPP,"
---

IP-CAN je konceptuální síť, která poskytuje IP konektivitu mezi uživatelským zařízením (User Equipment) a externí IP sítí a tvoří základ pro všechny služby založené na IP v systémech 3GPP.

## Popis

IP-Connectivity Access Network (IP-CAN) není jediný fyzický síťový prvek, ale logický architektonický koncept definovaný v rámci specifikací 3GPP. Představuje celou sadu síťových entit a funkcí, které společně vytvářejí a udržují IP přenosovou konektivitu pro uživatele. Tato konektivita začíná na uživatelském zařízení (UE) a prochází rádiovou přístupovou sítí (např. [UTRAN](/mobilnisite/slovnik/utran/), [E-UTRAN](/mobilnisite/slovnik/e-utran/), NG-RAN) a jádrem sítě (např. [GPRS](/mobilnisite/slovnik/gprs/) jádro, EPC, 5GC) až k bráně paketové datové sítě ([PDN](/mobilnisite/slovnik/pdn/) Gateway, [PGW](/mobilnisite/slovnik/pgw/)) v 4G nebo k funkci uživatelské roviny (User Plane Function, [UPF](/mobilnisite/slovnik/upf/)) v 5G, která slouží jako kotvící bod k externím IP sítím.

Z funkční perspektivy IP-CAN zahrnuje všechny vrstvy a protokoly zapojené do IP relace. To zahrnuje zřízení, modifikaci a ukončení přenosů (bearer) nebo QoS toků, které přenášejí IP provoz uživatele. Každá IP-CAN relace je spojena s konkrétní IP adresou UE a je jednoznačně identifikována pro účely řízení politiky a účtování. Architektura je v pozdějších verzích navržena jako nezávislá na typu přístupu, což znamená, že základní logika politiky může být aplikována jednotně, ať je uživatel připojen přes 3G, 4G, 5G nebo ne-3GPP přístup jako Wi-Fi.

Hlavní role IP-CAN je sloužit jako kontext pro architekturu řízení politiky a účtování ([PCC](/mobilnisite/slovnik/pcc/)). Funkce pravidel politiky a účtování ([PCRF](/mobilnisite/slovnik/pcrf/)) nebo funkce řízení politiky (PCF) v 5GC používá IP-CAN relaci jako klíčový kotvící bod pro aplikaci rozhodnutí o politice. PCRF/PCF přijímá informace o IP-CAN relaci (např. IP adresa, typ přístupu, charakteristiky výchozího přenosu) od síťového prvku, který funguje jako funkce vynucení politiky a účtování (PCEF), typicky PGW nebo UPF. Na základě profilů účastníka, požadavků služeb a stavu sítě pak PCRF/PCF instaluje dynamická PCC pravidla do PCEF. Tato pravidla řídí parametry QoS (jako garantovaný přenosový výkon), řízení provozu (povolení/blokování paketů) a metody účtování pro konkrétní toky služebních dat v rámci IP-CAN relace.

Klíčové komponenty podílející se na realizaci IP-CAN relace zahrnují UE, rádiovou přístupovou síť, obslužnou bránu (SGW) v EPC, PGW/UPF (která funguje jako koncový bod IP-CAN přenosu a jako PCEF) a PCRF/PCF. Rozhraní mezi těmito prvky, jako je rozhraní Gx (mezi PCRF a PGW) nebo rozhraní N7 (mezi PCF a SMF), se používají ke správě politik IP-CAN relace. Tento koncept je zásadní pro umožnění bezproblémových, kvalitativně zaručených a účtovatelných multimediálních služeb IP napříč vyvíjejícími se generacemi sítí.

## K čemu slouží

Koncept IP-CAN byl zaveden, aby poskytl standardizovaný, abstraktní model pro IP konektivitu v sítích 3GPP, což bylo zásadní při vývoji sítí od okruhově přepínaného hlasu k plně IP architekturám podporujícím bohaté multimediální služby. Před jeho formalizací bylo řízení QoS a účtování pro různé IP služby složité a často proprietární. Model IP-CAN vytvořil jasný demarkační bod a konzistentní kontext relace, což umožnilo vývoj jednotného rámce pro řízení politiky a účtování (PCC).

Jeho vytvoření vyřešilo kritický problém, jak dynamicky aplikovat síťové politiky (pro kvalitu služeb, řízení provozu a účtování) na IP relaci uživatele bez ohledu na podkladovou přístupovou technologii. Definováním IP-CAN relace mohli operátoři korelovat využití služeb uživatele (např. video stream) s jeho síťovým připojením, což umožnilo účtování citlivé na službu (jako zero-rating) a garantovanou šířku pásma pro prémiové služby. To byl klíčový faktor pro IP Multimedia Subsystem (IMS) a komerční datové tarify.

Navíc abstrakce IP-CAN zajistila budoucí kompatibilitu architektury politiky. S příchodem nových přístupových technologií (jako LTE a později 5G NR) mohla zůstat základní logika PCC do značné míry nezměněna pouhým aktualizováním definice parametrů IP-CAN relace pro daný nový typ přístupu. To umožnilo plynulý vývoj od 3G přes 4G k 5G při zachování konzistentní služební a obchodní logiky pro operátory.

## Klíčové vlastnosti

- Poskytuje logický model pro koncovou IP přenosovou konektivitu
- Slouží jako kotvící kontext pro rozhodnutí řízení politiky a účtování (PCC)
- Jednoznačně identifikuje IP relaci uživatele pro účely správy a účtování
- Navrženo jako nezávislé na přístupové technologii (3GPP i ne-3GPP)
- Umožňuje dynamické řízení QoS a detekci toků služebních dat
- Umožňuje bezproblémovou mobilitu a kontinuitu relace pro IP služby

## Související pojmy

- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)
- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [PCEF – Policy and Charging Enforcement Function](/mobilnisite/slovnik/pcef/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.417** (Rel-7) — IMS Core Component for NGN Architecture
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture
- **TS 23.701** (Rel-12) — WebRTC Access to IMS Architecture Study
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TS 23.802** (Rel-7) — Enhanced End-to-End QoS Architecture
- **TS 23.803** (Rel-7) — PCC Architecture Harmonization Study
- **TS 23.806** (Rel-7) — Voice Call Continuity between CS and IMS
- **TS 24.008** (Rel-19) — 3GPP TS 24008: Core Network Protocols
- **TS 24.147** (Rel-19) — IMS Conferencing Protocol Details
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.424** (Rel-19) — XCAP over Ut for Supplementary Services MO
- … a dalších 11 specifikací

---

📖 **Anglický originál a plná specifikace:** [IP-CAN na 3GPP Explorer](https://3gpp-explorer.com/glossary/ip-can/)
