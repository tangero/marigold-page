---
slug: "rto"
url: "/mobilnisite/slovnik/rto/"
type: "slovnik"
title: "RTO – Remote Transcoder Operation"
date: 2025-01-01
abbr: "RTO"
fullName: "Remote Transcoder Operation"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/rto/"
summary: "Síťová architektura, ve které jsou funkce převodu řečových kodeků přesunuty z ústředny mobilního spojení (MSC) na vyhrazený uzel nebo blíže k okraji sítě. Tím se optimalizuje zpracování hlasového prov"
---

RTO je síťová architektura, ve které jsou funkce převodu řečových kodeků přesunuty z ústředny mobilního spojení (MSC) na vyhrazený uzel nebo k okraji sítě za účelem optimalizace provozu, snížení nákladů a zlepšení kvality hlasu.

## Popis

Remote Transcoder Operation (RTO) je síťová funkce definovaná v 3GPP TS 23.231, která přesouvá převodní jednotku (TCU) pro řečové kodeky z tradiční ústředny mobilního spojení ([MSC](/mobilnisite/slovnik/msc/)) na samostatný síťový uzel, často umístěný blíže k rádiové přístupové síti. Převod kodeku je nezbytný, když hlasové hovory používají různé kodeky, například mezi legacy okruhově spínanou sítí používající [AMR](/mobilnisite/slovnik/amr/) (Adaptive Multi-Rate) a paketově spínanou sítí používající [AMR-WB](/mobilnisite/slovnik/amr-wb/) (Wideband) nebo jiné kodeky. V RTO je TCU nasazena vzdáleně, což umožňuje MSC obejít převod kodeku u hovorů používajících kompatibilní kodeky, čímž se snižuje procesní zátěž a zlepšuje kvalita hlasu.

Architektonicky RTO zavádí dva klíčové uzly: Remote Transcoder Unit (RTU) a Transcoder Control Function (TCF). RTU provádí vlastní převod řečového kodeku, zatímco TCF, která může být integrována s MSC nebo funkcí řízení mediální brány ([MGCF](/mobilnisite/slovnik/mgcf/)), řídí činnost RTU na základě signalizace hovoru. Během sestavování hovoru MSC určí, zda je převod kodeku potřeba, porovnáním kodeků podporovaných volající a volanou stranou. Pokud je převod vyžadován, MSC instruuje TCF k alokaci prostředku RTU a směruje hlasový přenosový kanál přes něj. Pokud ne, může být hlasová cesta zřízena přímo mezi koncovými body, čímž se vyhnou zbytečným převodům kodeků.

Princip fungování RTO zahrnuje oddělení signalizace a přenosové cesty. Řídicí signalizace hovoru (např. přes [ISUP](/mobilnisite/slovnik/isup/) nebo BICC) stále prochází MSC, ale uživatelská rovina (hlasový provoz) může být směrována přímo mezi řadič rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)) nebo základnovou stanicí a RTU, nebo dokonce peer-to-peer, pokud převod kodeku není potřeba. To se často implementuje pomocí principů TrFO (Transcoder Free Operation) a [TFO](/mobilnisite/slovnik/tfo/) (Tandem Free Operation). RTO snižuje počet stupňů kódování/dekódování (tandemové kódování), které mohou degradovat kvalitu hlasu kvůli kvantizačnímu šumu. Umístěním převodníků vzdáleně mohou operátoři tyto prostředky efektivně sdružovat, škálovat je nezávisle na MSC a optimalizovat přenosovou šířku pásma, zejména v sítích přecházejících na VoIP a IMS.

## K čemu slouží

RTO bylo vyvinuto k řešení neefektivit v tradičních okruhově spínaných hlasových sítích, kde byly převodníky fyzicky integrovány do každé [MSC](/mobilnisite/slovnik/msc/). Tato architektura nutila veškerý hlasový provoz procházet převodníkem MSC, i když obě větve hovoru používaly stejný kodek, což vedlo k zbytečnému převodu (tandemovému kódování), který zhoršoval kvalitu hlasu a spotřebovával dodatečné hardwarové prostředky. Mezi omezení patřily zvýšená latence, vyšší náklady na zařízení a suboptimální kvalita hlasu, zejména s příchodem širokopásmových kodeků jako AMR-WB pro zlepšení uživatelského zážitku.

Jeho vytvoření bylo motivováno evolucí směrem k plně IP sítím a snahou optimalizovat zpracování hlasu ve smíšených síťových prostředích (2G/3G/4G). Když operátoři nasazovali paketově spínaná jádra a IMS, potřebovali způsob, jak řešit vzájemné propojení mezi legacy okruhově spínanými kodeky a VoIP kodeky bez nutnosti převodu pro každý hovor. RTO to řeší oddělením převodní funkce, což umožňuje flexibilní umístění a použití na vyžádání. Tím se snižují provozní náklady centralizací a sdružováním prostředků převodníků a zlepšuje se kvalita hlasu umožněním provozu bez převodníku, kdykoli je to možné.

Historicky, před RTO, sítě spoléhaly na pevná umístění převodníků, což komplikovalo zavádění nových kodeků a omezovalo škálovatelnost. Standardizace v Release 8 poskytla rámec pro vzdálené řízení převodníku v souladu s širšími trendy, jako je virtualizace síťových funkcí a edge computing. RTO řeší problém neefektivního využití prostředků a degradace kvality v prostředích s více kodeky, usnadňuje plynulejší migraci na IP hlasové služby jako VoLTE a VoNR při zachování zpětné kompatibility s legacy systémy.

## Klíčové vlastnosti

- Oddělení převodních funkcí od MSC na vzdálené uzly pro flexibilní nasazení
- Podpora TrFO (Transcoder Free Operation) pro vyhýbání se zbytečným převodům kodeků
- Centralizované řízení pomocí Transcoder Control Function (TCF) pro dynamickou alokaci prostředků
- Kompatibilita s více řečovými kodeky včetně AMR, AMR-WB a EVS
- Optimalizace přenosové šířky pásma snížením výskytů tandemového kódování
- Bezproblémové vzájemné propojení mezi okruhově spínanými a paketově spínanými hlasovými sítěmi

## Související pojmy

- [TFO – Tandem Free Operation](/mobilnisite/slovnik/tfo/)

## Definující specifikace

- **TS 23.231** (Rel-19) — SIP-I based CS core network stage 2

---

📖 **Anglický originál a plná specifikace:** [RTO na 3GPP Explorer](https://3gpp-explorer.com/glossary/rto/)
