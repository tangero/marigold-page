---
slug: "spne"
url: "/mobilnisite/slovnik/spne/"
type: "slovnik"
title: "SPNE – Signal Processing Network Equipment"
date: 2025-01-01
abbr: "SPNE"
fullName: "Signal Processing Network Equipment"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/spne/"
summary: "Síťová funkce definovaná v rámci funkce Media Resource Function (MRF) IP Multimedia Subsystem (IMS). Je zodpovědná za zpracování mediálních proudů a poskytuje schopnosti jako převod kódování audio/vid"
---

SPNE je síťová funkce v rámci funkce IMS Media Resource Function, která zpracovává mediální proudy a poskytuje schopnosti jako převod kódování audio/video a mixování pro služby například konferenční hovory.

## Popis

Signal Processing Network Equipment (SPNE) je logická entita specifikovaná jako část Media Resource Function Processor ([MRFP](/mobilnisite/slovnik/mrfp/)) v architektuře 3GPP IMS. Jejím hlavním úkolem je provádět operace digitálního zpracování signálu ([DSP](/mobilnisite/slovnik/dsp/)) v reálném čase na mediálních proudech – typicky audio a video – které jsou směrovány přes jádro IMS. SPNE řeší úlohy jako převod kódování (např. konverze mezi kodeky [AMR-NB](/mobilnisite/slovnik/amr-nb/) a [EVS](/mobilnisite/slovnik/evs/)), mixování audio pro konference s více účastníky, generování tónů (např. vyzváněcí tón, tón obsazení), rozpoznávání řeči pro systémy interaktivní hlasové odpovědi ([IVR](/mobilnisite/slovnik/ivr/)) a analýzu média (např. potlačení ticha, detekce hlasové aktivity). Funguje pod kontrolou Media Resource Function Controller ([MRFC](/mobilnisite/slovnik/mrfc/)), který používá protokoly jako H.248 (Megaco) k instruování SPNE, které zpracování použít na konkrétní mediální relace.

Architektonicky je SPNE klíčovou součástí [MRF](/mobilnisite/slovnik/mrf/), která je sama částí platformy pro poskytování služeb IMS. MRFC funguje jako mozek, přijímající servisní logiku od Application Server ([AS](/mobilnisite/slovnik/as/)) přes ISC rozhraní, zatímco SPNE funguje jako síla, vykonávající mediální manipulace. Když je iniciována služba jako konferenční hovor, MRFC na základě instrukcí od AS vytvoří kontrolní asociace s jedním nebo více SPNE. Přikazuje jim alokovat zdroje, vytvořit mixující jednotky a použít potřebné kodeky. Mediální proudy od účastníků jsou pak směrovány (přes jádro IMS a potenciálně přes Access Gateway) do SPNE, které zpracuje je a posílá zpět kombinovaný nebo transformovaný proud. Toto oddělení kontroly (MRFC) a zpracování (SPNE) umožňuje škálovatelnou a flexibilní mediální službu.

Jak SPNE funguje zahrnuje komplexní interakci s podkladovou transportní a signalizační plochou. Typicky komunikuje s jádrem síťě pomocí IP transportu (např. RTP/RTCP pro média) a může podporovat virtualizaci síťových funkcí (NFV). Klíčové interní komponenty SPNE obsahují digitální procesory signálu (hardwarové nebo softwarové), knihovny kodeků, mixující enginy a jednotky zpracování paketů. Jeho role je kritická pro kontinuitu služby a kvalitu v heterogenních síťích, kde UE mohou podporovat různé kodeky nebo mají různou kapacitu bandwidth. Poskytováním centralizovaného zpracování média SPNE umožňuje pokročilé služby bez nutnosti všech endpointů mít stejné schopnosti, tím zajišťuje interoperabilitu a konzistentní uživatelský experience. Specifikace TS 29.333 definuje Mn rozhraní mezi MRFC a MRFP (které obsahuje SPNE), detailně popisující balíčky a příkazy pro mediální kontrolu.

## K čemu slouží

SPNE bylo vytvořeno pro řešení potřeb pokročilého, síťového zpracování média v all-IP telekomunikačních síťích, specificně v rámci frameworku IMS. Jak se mobilní síťě vyvinuly z circuit-switched hlasu na packet-switched multimediální služby, byla potřeba podporovat funkce jako konference s více účastníky, převod kódování mezi různými kodeky a interaktivní mediální služby, které byly tradičně řešeny specializovaným equipmentem v legacy síťích (např. konferenční bridge v PSTN). SPNE poskytuje standardizovaný, škálovatelný způsob poskytování těchto schopností jako síťová služba, řeší problém heterogenity endpointů a umožňuje rich communication services.

Historicky, v pre-IMS síťích, zpracování média bylo často těsně spojeno s switching infrastrukturou nebo implementované proprietárním, ne-interoperabilním způsobem. Motivace pro definování SPNE v 3GPP Release 8 byla oddělení zpracování média od call control a session management jako část architektury IMS, která je založená na principu oddělení kontrolní, mediální a aplikační plochy. Toto oddělení umožňuje operatorům deployovat a škálovat mediální zdroje nezávisle, redukuje náklady pomocí poolingu zdrojů a podporuje inovaci umožněním third-party application serverů využívat standardizované mediální zpracování funkcí. SPNE řeší limity předchozích přístupů poskytováním uniformního rozhraní (přes H.248) pro kontrolu širokého spektra mediálních zpracování úloh, zajišťující že služby jako video konference nebo unified messaging mohou být deployované konzistentně přes multi-vendor síťě.

## Klíčové vlastnosti

- Provádí úlohy zpracování média v reálném čase jako převod kódování, mixování a generování tónů
- Funguje jako část Media Resource Function Processor (MRFP) v IMS
- Kontrolovaný MRFC pomocí protokolu H.248 (Megaco) přes Mn rozhraní
- Umožňuje pokročilé služby jako audio/video konference a interaktivní hlasová odpověď
- Podporuje interoperabilitu mezi endpointy s různými schopnostmi kodeků
- Specifikované v 3GPP TS 29.333 pro kontrolní procedury a balíčky

## Definující specifikace

- **TS 29.333** (Rel-19) — MRFC-MRFP Mp Interface Protocol

---

📖 **Anglický originál a plná specifikace:** [SPNE na 3GPP Explorer](https://3gpp-explorer.com/glossary/spne/)
