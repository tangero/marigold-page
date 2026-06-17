---
slug: "n5cw"
url: "/mobilnisite/slovnik/n5cw/"
type: "slovnik"
title: "N5CW – Non 5G Capable over WLAN"
date: 2026-01-01
abbr: "N5CW"
fullName: "Non 5G Capable over WLAN"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/n5cw/"
summary: "N5CW je indikátor schopnosti UE, který značí, že zařízení podporuje připojení k 5G Core síti, ale není schopno využít 5G radiový přístup (NG-RAN) přes rozhraní WLAN. V podstatě označuje UE, které může"
---

N5CW je indikátor schopnosti UE, který značí, že zařízení podporuje připojení k 5G Core, ale nemůže využít 5G radiový přístup přes rozhraní WLAN.

## Popis

Non 5G Capable over WLAN (N5CW) je indikátor schopnosti spojený s uživatelským zařízením (UE) v systému 5G. Jedná se o specifický parametr v rámci informací o síťových schopnostech UE, který je sdělován síti během registračních procedur. Termín explicitně označuje omezení: UE deklarující N5CW je schopno se připojit k 5G Core síti (5GC), ale postrádá schopnost využívat technologii 5G New Radio (NR), když pracuje přes rozhraní Wireless Local Area Network (WLAN). Prakticky to často odkazuje na UE s modulem WLAN (Wi-Fi), které může toto WLAN rozhraní použít pro datovou konektivitu, ale nemůže stejné WLAN rozhraní použít pro připojení k buňce 5G NR (např. přes [NR-U](/mobilnisite/slovnik/nr-u/), NR v nelicencovaném spektru nebo 5G rádiový spoj prezentovaný jako WLAN).

Z architektonického hlediska tato schopnost ovlivňuje chování UE a sítě ve scénářích zahrnujících propojení WLAN a 5G. Když je UE se schopností N5CW připojeno přes WLAN přístupovou síť (a potenciálně registrované v 5GC přes [N3IWF](/mobilnisite/slovnik/n3iwf/)), síť chápe, že této UE nelze nařídit ani od ní očekávat použití procedur 5G NR přes tento WLAN spoj. To ovlivňuje funkce jako politiky Access Network Discovery and Selection Function ([ANDSF](/mobilnisite/slovnik/andsf/)), UE Route Selection Policy (URSP) a příkazy správy mobility. Například síť se nepokusí o předání této UE z 3GPP přístupu (4G/5G) na buňku 5G NR hostovanou na WLAN infrastruktuře, protože UE indikovalo, že tuto specifickou schopnost postrádá.

Indikátor N5CW funguje ve spojení s dalšími příznaky schopností UE. Je součástí sady indikátorů popisujících podporované přístupové technologie a schopnosti propojení UE, jako je "5G Capable" nebo podpora "Wireless and Wireline Convergence" (WWC). Během registrace nebo aktualizace schopností UE zahrnuje tuto informaci ve svých [NAS](/mobilnisite/slovnik/nas/) zprávách pro [AMF](/mobilnisite/slovnik/amf/). AMF pak tuto schopnost uloží a může ji sdílet s dalšími síťovými funkcemi, jako je [SMF](/mobilnisite/slovnik/smf/) nebo [PCF](/mobilnisite/slovnik/pcf/). Tyto funkce mohou použít příznak N5CW k přizpůsobení síťových politik. Například pokud UE indikuje N5CW, politika mobility může upřednostnit jeho setrvání na 4G LTE nebo 5G NR makro buňce spíše než pokus o přesměrování na WLAN síť, která tvrdí, že nabízí 5G NR přístup, protože UE by nebylo schopno využít 5G NR komponentu.

Z pohledu protokolu je N5CW definováno v 3GPP TS 24.501 (NAS) jako součást informací o síťových schopnostech UE. Jeho přítomnost signalizuje 5G Core specifické omezení, což umožňuje inteligentnější a efektivnější výběr radiové přístupové technologie, přidělování prostředků a správu kontinuity služeb v heterogenních sítích, kde koexistuje více typů radiových a neradiových přístupových technologií.

## K čemu slouží

Indikátor schopnosti N5CW byl zaveden, aby řešil nejednoznačnost a potenciální neefektivitu v chování sítě a UE v rámci stále složitějších heterogenních rádiových prostředí. S vývojem nasazení 5G se objevily nové scénáře, jako je provoz 5G NR v nelicencovaných pásmech (5G [NR-U](/mobilnisite/slovnik/nr-u/)) nebo integrovaný přístupový přenos (IAB), kde by se hranice mezi "WLAN" a "5G rádiem" mohla z pohledu UE rozmazat. UE může podporovat WLAN pro přístup k internetu, ale nepodporovat specifické protokoly potřebné k tomu, aby bylo WLAN signálem zacházeno jako s nosičem 5G NR. Bez explicitní signalizace by síť mohla předpokládat, že UE připojené přes WLAN může být předáno na buňku 5G NR na stejném WLAN, což by vedlo k neúspěšným procedurám a zhoršenému uživatelskému zážitku.

Primární problém, který N5CW řeší, je umožnění přesného vyjednávání schopností mezi UE a 5G Core. Poskytuje jasnost ohledně rádiových schopností UE přes WLAN rozhraní a zabraňuje síti v chybných předpokladech během výběru přístupu, směrování provozu (např. ATSSS) a rozhodování o předání. To je obzvláště důležité pro optimalizaci výkonu sítě a využití prostředků; pokus o předání na technologii, kterou UE nemůže použít, plýtvá signalizačními prostředky a způsobuje přerušení služby.

Historicky se signalizace schopností UE zaměřovala na širokou podporu rádiových přístupových technologií (např. E-UTRA, NR). Zavedení N5CW odráží realitu 5G-Advanced a konvergence, která je více nuancovaná, kde mohou být různá fyzická rozhraní (jako WLAN) použita více způsoby (jako čistý non-3GPP IP přístup nebo jako transportní vrstva vrstvy 2 pro 3GPP rádio). Explicitním uvedením "non 5G capable over WLAN" informuje UE síť o svých omezeních, což umožňuje chytřejší správu mobility. To bylo motivováno potřebou zajistit robustní kontinuitu služeb a efektivní správu rádiových prostředků, když operátoři nasazují multi-přístupové sítě kombinující 4G, 5G, Wi-Fi 6/6E/7 a další technologie.

## Klíčové vlastnosti

- Příznak schopnosti UE indikující nedostatek schopnosti 5G NR rádiového rozhraní přes své WLAN rozhraní
- Signalizováno UE směrem k AMF během registračních procedur nebo procedur aktualizace schopností
- Ovlivňuje síťové politiky pro výběr přístupu, směrování provozu (ATSSS) a řízení předání
- Zabraňuje síti v pokusech o neplatné příkazy mobility na 5G NR přes WLAN
- Umožňuje přesnější přidělování prostředků a správu kontinuity služeb v heterogenních sítích
- Definováno v rámci informací o síťových schopnostech UE v NAS signalizaci (TS 24.501)

## Související pojmy

- [NR-U – New Radio Unlicensed](/mobilnisite/slovnik/nr-u/)
- [ATSSS – Access Traffic Steering, Switching, and Splitting](/mobilnisite/slovnik/atsss/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)

## Definující specifikace

- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 29.214** (Rel-19) — Policy and Charging Control over Rx
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures

---

📖 **Anglický originál a plná specifikace:** [N5CW na 3GPP Explorer](https://3gpp-explorer.com/glossary/n5cw/)
