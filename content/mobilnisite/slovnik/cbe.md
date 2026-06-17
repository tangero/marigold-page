---
slug: "cbe"
url: "/mobilnisite/slovnik/cbe/"
type: "slovnik"
title: "CBE – Cell Broadcast Entity"
date: 2026-01-01
abbr: "CBE"
fullName: "Cell Broadcast Entity"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cbe/"
summary: "Cell Broadcast Entity (CBE) je síťový prvek zodpovědný za vytváření a správu zpráv služby Cell Broadcast Service (CBS). Spolupracuje s Cell Broadcast Center (CBC) za účelem doručování varovných zpráv"
---

CBE je síťový prvek zodpovědný za vytváření a správu zpráv služby Cell Broadcast Service pro doručení všem mobilním zařízením v určitých geografických oblastech.

## Popis

Cell Broadcast Entity (CBE) je základní funkční komponenta v architektuře 3GPP určená pro službu Cell Broadcast Service ([CBS](/mobilnisite/slovnik/cbs/)). Působí jako výchozí bod pro vysílání zpráv, což jsou typicky textová upozornění určená pro současné doručení všem uživatelským zařízením (UE) v rámci jedné nebo více určených buněk. CBE není standardizovaný fyzický uzel, ale logická funkce, která může být implementována v rámci sítě operátora nebo externími poskytovateli služeb, například vládními agenturami pro systémy varování veřejnosti. Jejím hlavním úkolem je vytvářet, formátovat a předávat zprávy CBS do Cell Broadcast Center ([CBC](/mobilnisite/slovnik/cbc/)) pro další distribuci prostřednictvím rádiové přístupové sítě.

Z architektonického hlediska se CBE připojuje k CBC prostřednictvím standardizovaného rozhraní, obvykle za použití protokolů jako Cell Broadcast Service Application Programming Interface (CBS-API) nebo jiných proprietárních rozhraní definovaných pro odesílání zpráv. CBE je zodpovědná za definování klíčových parametrů vysílané zprávy. Mezi tyto parametry patří identifikátor zprávy (který udává typ zprávy, například varování před zemětřesením nebo Amber Alert), sériové číslo (pro správu verzí zpráv a detekci duplicit), geografický rozsah (definovaný seznamem identifikátorů buněk nebo servisních oblastí), plán opakování vysílání a samotný obsah zprávy, který má omezenou délku (např. 93 nebo 1395 znaků v závislosti na kódovacím schématu).

Po přijetí žádosti o zprávu od CBE CBC žádost ověří, spravuje plán vysílání a přepošle zprávu příslušným řadičům základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) v sítích 2G/3G nebo entitám Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v síti 4G, které následně instruují základnové stanice (NodeB nebo eNodeB), aby zprávu vysílaly přes rozhraní vzduch. CBE může také od CBC přijímat hlášení o doručení nebo oznámení o chybách, což umožňuje původci zprávy sledovat stav vysílání. V moderních implementacích, zejména pro systémy varování veřejnosti (PWS), jako je Earthquake and Tsunami Warning System (ETWS) a Commercial Mobile Alert System ([CMAS](/mobilnisite/slovnik/cmas/)), CBE často zahrnuje pokročilé funkce pro stanovení priority zpráv, geografické cílení, výběr jazyka a integraci s národními varovnými autoritami.

Fungování CBE se řídí specifikacemi jako je 3GPP TS 23.041 (Technical Realization of Cell Broadcast Service). Její návrh zajišťuje efektivní doručování vysílaných zpráv bez zahlcení sítě, neboť využívá samostatný logický kanál (Cell Broadcast Channel, [CBCH](/mobilnisite/slovnik/cbch/)), který nenarušuje point-to-point provoz. Díky tomu je CBS ideální pro časově kritické, neinteraktivní šíření informací, kde jsou prvořadá spolehlivost a široký dosah.

## K čemu slouží

Cell Broadcast Entity byla vytvořena, aby umožnila spolehlivou a síťově efektivní metodu vysílání informací všem mobilním uživatelům v určité geografické oblasti. Před zavedením [CBS](/mobilnisite/slovnik/cbs/) se hromadná oznámení spoléhala na službu Short Message Service (SMS), což je point-to-point technologie. Odesílání jednotlivých SMS tisícům či milionům uživatelů v cílové oblasti způsobuje výrazné signalizační přetížení, zpoždění a potenciální kolaps sítě během mimořádných událostí – problém známý jako SMS congestion. CBE a širší architektura CBS tento problém řeší použitím one-to-many vysílacího mechanismu, který přenáší jedinou zprávu jednou na buňku, a ta je pak přijata všemi kompatibilními zařízeními v pokrytí této buňky, čímž se eliminuje signalizační režie na jednoho uživatele.

Historicky byla CBS původně definována ve standardech GSM (2G) pro komerční služby jako dopravní aktualizace nebo reklama. Její klíčový význam byl však rozpoznán pro veřejnou bezpečnost po velkých katastrofách, kdy komunikační sítě selhaly. To motivovalo vylepšení CBS pro nouzová upozornění, což vedlo ke standardizovaným systémům varování veřejnosti (PWS) v 3GPP Release 9. CBE slouží jako vstupní bod pro oprávněné subjekty (například vládní agentury) k vkládání těchto životně důležitých upozornění do mobilní sítě. Řeší tak omezení předchozích metod varování, které byly pomalé, nespolehlivé nebo postrádaly přesné geografické cílení.

Dále CBE poskytuje standardizované rozhraní, které odděluje původce zprávy (varovnou autoritu) od infrastruktury síťového operátora ([CBC](/mobilnisite/slovnik/cbc/) a rádiová síť). Toto oddělení umožňuje zabezpečený, kontrolovaný přístup externím agenturám při zachování integrity sítě. Tato technologie zajišťuje, že naléhavá varování před událostmi, jako jsou zemětřesení, tsunami, extrémní počasí nebo únosy dětí (AMBER alerts), mohou být okamžitě a spolehlivě doručena postiženému obyvatelstvu, a to i když jsou hlasové a datové služby přetížené, čímž zachraňuje životy a zvyšuje veřejnou bezpečnost.

## Klíčové vlastnosti

- Vytváří a formátuje zprávy služby Cell Broadcast Service (CBS) pro síťové doručení
- Definuje parametry vysílání včetně geografického rozsahu (seznam buněk), identifikátoru zprávy a plánu opakování
- Spolupracuje s Cell Broadcast Center (CBC) pomocí standardizovaných protokolů (např. CBS-API)
- Podporuje systémy varování veřejnosti (PWS) jako ETWS a CMAS pro nouzová upozornění
- Umožňuje geograficky cílené doručování zpráv do specifických buněk nebo servisních oblastí
- Poskytuje stanovení priority zpráv a zpracování pro kritická upozornění

## Definující specifikace

- **TS 22.268** (Rel-20) — Public Warning System (PWS) Requirements
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TR 33.969** (Rel-19) — Security for Public Warning System (PWS)
- **TS 48.049** (Rel-19) — Cell Broadcast Service Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [CBE na 3GPP Explorer](https://3gpp-explorer.com/glossary/cbe/)
