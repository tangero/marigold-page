---
slug: "tmr"
url: "/mobilnisite/slovnik/tmr/"
type: "slovnik"
title: "TMR – Transmission Medium Requirement"
date: 2025-01-01
abbr: "TMR"
fullName: "Transmission Medium Requirement"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tmr/"
summary: "Parametr v architektuře 3GPP Bearer Binding and Event Reporting Function (BBERF) a Policy and Charging Control (PCC). Specifikuje požadované charakteristiky QoS pro přenosovou cestu (bearer) přenášejí"
---

TMR je parametr v architektuře 3GPP PCC, který specifikuje požadované charakteristiky kvality služby (QoS) pro přenosovou cestu (bearer) přenášející IP toky, což umožňuje vynucování politik a alokaci zdrojů.

## Popis

Transmission Medium Requirement (TMR) je technický parametr definovaný v kontextu architektury 3GPP Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)), konkrétně pro interakce zahrnující funkci Bearer Binding and Event Reporting Function ([BBERF](/mobilnisite/slovnik/bberf/)). BBERF je funkční entita typicky umístěná v přístupové bráně (např. Serving Gateway v [E-UTRAN](/mobilnisite/slovnik/e-utran/), [PDN](/mobilnisite/slovnik/pdn/) Gateway v non-3GPP přístupu), která je zodpovědná za vazbu přenosových cest (bearer binding), ověření vazby pro uplink a hlášení událostí funkci Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)). TMR je klíčová informace předávaná z BBERF do PCRF za účelem vyžádání nebo nahlášení požadovaných QoS zdrojů pro konkrétní služební datový tok nebo agregát toků.

Operačně, když je detekován nový služební datový tok nebo když se změní podmínky QoS v přístupové síti, BBERF sestaví TMR. Tento TMR obsahuje podrobné atributy QoS nezbytné pro PCRF, aby mohla činit informovaná rozhodnutí o politikách. Tyto atributy typicky zahrnují QoS Class Identifier ([QCI](/mobilnisite/slovnik/qci/)), Allocation and Retention Priority ([ARP](/mobilnisite/slovnik/arp/)), Guaranteed Bit Rate ([GBR](/mobilnisite/slovnik/gbr/)) pro GBR přenosové cesty, Maximum Bit Rate (MBR) a potenciálně Aggregate Maximum Bit Rate (AMBR). BBERF odesílá tento TMR do PCRF v rámci zprávy Gxx relace, jako je Credit Control Request (CCR). PCRF používá TMR spolu s informacemi z profilu účastníka, filtry služebních datových toků a operátorsky definovanými politikami k vytvoření nebo úpravě odpovídajících pravidel Policy and Charging Control (PCC).

Vytvořená PCC pravidla, která zahrnují autorizované parametry QoS, jsou poté zřízena do funkce Policy and Charging Enforcement Function (PCEF) a také sdělena zpět BBERF. To umožňuje BBERF provést vazbu přenosové cesty (bearer binding) – namapovat autorizovanou QoS z PCC pravidla na odpovídající podkladovou přístupově specifickou přenosovou cestu (např. EPS bearer v LTE). Mechanismus TMR zajišťuje, že PCRF má přesné informace v reálném čase o přenosových schopnostech a požadavcích přístupové sítě, což umožňuje dynamické a relaci-uvědomující řízení politik. Je klíčovým prvkem pro koordinaci QoS mezi vrstvou politik v jádrové síti a správou zdrojů v rádiové přístupové síti.

## K čemu slouží

Koncept TMR byl vyvinut k řešení výzvy centralizovaného řízení politik v architektuře sítě založené na IP tocích a více přístupech, zavedené s EPS a rozšířeným PCC. Před PCC bylo QoS a správa přenosových cest často staticky konfigurováno nebo řízeno decentralizovaně v rámci každé přístupové sítě, což vedlo k potenciálním nekonzistencím, neefektivnímu využití zdrojů a neschopnosti aplikovat sofistikované, službou-uvědomující politiky napříč různými typy přístupu. Vznikla potřeba standardizovaného rozhraní a informačního modelu, který by umožnil přístupové bráně (BBERF) komunikovat své specifické požadavky na zdroje do centrálního bodu pro rozhodování o politikách (PCRF).

TMR řeší problém abstrakce přístupově specifických charakteristik přenosových cest do generické sady parametrů QoS, kterou může PCRF zpracovat. Umožňuje síti dynamicky vyžadovat zdroje na základě požadavků služeb v reálném čase, jako je zahájení VoIP hovoru nebo videoproudu, namísto spoléhání se na předem zřízené statické přenosové cesty. To bylo motivováno evolucí směrem k plně IP sítím a požadavkem na bezproblémovou kontinuitu služeb a konzistentní vynucování QoS, ať je uživatel na LTE, 3G nebo důvěryhodném non-3GPP přístupu. TMR usnadňuje roli PCRF jako mozku systému PCC tím, že jí poskytuje nezbytné vstupy pro činění inteligentních rozhodnutí, která vyvažují uživatelský zážitek, efektivitu sítě a operátorské politiky.

## Klíčové vlastnosti

- Předává požadavky QoS (QCI, ARP, GBR, MBR) z přístupové sítě do PCRF
- Používá se v rozhraní referenčního bodu Gxx mezi BBERF a PCRF
- Umožňuje dynamickou vazbu přenosových cest (bearer binding) a generování pravidel politik
- Podporuje požadavky na zdroje pro GBR i Non-GBR přenosové cesty
- Nezbytný pro rozhodnutí o řízení politik a účtování s ohledem na přístup (access-aware)
- Spouští procedury modifikace IP-CAN relace iniciované PCRF

## Související pojmy

- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [BBERF – Bearer Binding and Event Reporting Function](/mobilnisite/slovnik/bberf/)
- [PCEF – Policy and Charging Enforcement Function](/mobilnisite/slovnik/pcef/)
- [QCI – Quality of Service Class Identifier](/mobilnisite/slovnik/qci/)

## Definující specifikace

- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 29.235** (Rel-19) — SIP-I CS Core Network Interworking

---

📖 **Anglický originál a plná specifikace:** [TMR na 3GPP Explorer](https://3gpp-explorer.com/glossary/tmr/)
