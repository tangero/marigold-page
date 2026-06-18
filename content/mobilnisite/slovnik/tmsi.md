---
slug: "tmsi"
url: "/mobilnisite/slovnik/tmsi/"
type: "slovnik"
title: "TMSI – Temporary Mobile Subscriber Identifier"
date: 2025-01-01
abbr: "TMSI"
fullName: "Temporary Mobile Subscriber Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tmsi/"
summary: "Dočasný, náhodně přidělený identifikátor, který nahrazuje trvalý International Mobile Subscriber Identity (IMSI) pro identifikaci UE na rozhraní rádiového přenosu. Zvyšuje soukromí a bezpečnost účastn"
---

TMSI (dočasný identifikátor účastníka mobilní sítě) je dočasný, náhodně přidělený identifikátor, který na rozhraní rádiového přenosu nahrazuje trvalý IMSI, čímž zvyšuje soukromí a bezpečnost účastníka tím, že brání sledování a odposlechu.

## Popis

Temporary Mobile Subscriber Identity (TMSI) je základní mechanismus pro ochranu soukromí a bezpečnost v mobilních sítích 2G (GSM), 3G (UMTS) a 4G (LTE). Jedná se o dočasný, lokálně platný identifikátor, který přiděluje navštívená ústředna [MSC](/mobilnisite/slovnik/msc/) (Visited Mobile Switching Center) v okruhově spínaných ([CS](/mobilnisite/slovnik/cs/)) doménách nebo entita [MME](/mobilnisite/slovnik/mme/) (Mobility Management Entity) v paketově spínané ([PS](/mobilnisite/slovnik/ps/)/EPS) doméně mobilní stanici nebo uživatelskému zařízení (UE) v rámci své oblasti působnosti. Primárním účelem TMSI je zabránit častému přenosu trvalého, globálně jedinečného International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)) přes rozhraní rádiového přenosu, což by umožnilo snadnou identifikaci a sledování účastníků.

Životní cyklus TMSI začíná, když se UE poprvé připojí k síti nebo vstoupí do nové oblasti polohy ([LA](/mobilnisite/slovnik/la/)) nebo sledovací oblasti ([TA](/mobilnisite/slovnik/ta/)). Během úvodní procedury aktualizace polohy nebo připojení se může UE potřebovat identifikovat pomocí svého IMSI. Po úspěšném ověření síť (MSC nebo MME) přidělí nové TMSI a zašle jej UE v zabezpečené zprávě, typicky zašifrované pomocí šifrovacích klíčů stanovených během ověřování. UE toto TMSI uloží do své nevolatilní paměti. Pro všechna následující signalizační spojení se sítí v rámci této oblasti – jako je odpověď na paging, provedení periodické aktualizace nebo zahájení volání iniciovaného mobilním zařízením – používá UE TMSI namísto IMSI. Síť udržuje mapování mezi přiděleným TMSI a IMSI účastníka ve své lokální databázi (kontext [VLR](/mobilnisite/slovnik/vlr/) nebo MME).

Struktura TMSI je navržena tak, aby měl význam pouze v oblasti řízené přidělujícím uzlem a po omezenou dobu. Může být periodicky znovu přidělen (např. při každé aktualizaci polohy) nebo v konkrétních scénářích, jako je předávání spojení mezi MSC. Pokud UE nemůže předložit platné TMSI (např. po ztrátě pokrytí nebo pokud síť nedokáže jej dekódovat), síť vyžádá IMSI v proceduře Identity Request, což spustí nové přidělení TMSI. V 4G LTE je tento koncept rozšířen o Globally Unique Temporary Identity (GUTI), který zahrnuje identifikátor MME (GUMMEI) a dočasný identifikátor (M-TMSI), čímž poskytuje širší rozsah. Mechanismus TMSI je základním kamenem bezpečnosti mobilních sítí, který spolupracuje s procedurami ověřování, šifrování a aktualizace polohy na ochraně důvěrnosti identity účastníka.

## K čemu slouží

TMSI byl zaveden v raných standardech GSM, aby řešil zásadní nedostatek v oblasti soukromí: trvalý IMSI, který globálně jednoznačně identifikuje účastníka, byl původně odesílán v nešifrované podobě přes rádiový kanál pro identifikaci. To umožňovalo pasivním odposlouchávačům snadno shromažďovat IMSI, sledovat pohyb osob a klonovat předplatná. Motivací bylo poskytnout určitou úroveň anonymity mobilním uživatelům, což byl problém rostoucí s rozšířením celulární technologie. TMSI vytvořil zásadní vrstvu ochrany soukromí tím, že zajistil, že trvalá identita je odhalena pouze při počátečním vstupu do sítě nebo v poruchových scénářích, nikoli během běžné komunikace.

Před zavedením TMSI absence dočasného identifikátoru umožňovala snadnou korelaci provozu účastníka a ohrožovala soukromí jeho polohy. Mechanismus TMSI to vyřešil implementací důvěrnosti identity. Jeho návrh byl veden potřebou lehkého, efektivního řešení, které by mohlo být integrováno do stávajících signalizačních procedur bez velké režie. Dočasná, lokální povaha TMSI znamená, že i když je zachycen, nelze jej použít k identifikaci účastníka mimo konkrétní síťovou oblast a časové okno. Tento koncept byl tak úspěšný, že byl převzat a vylepšen v UMTS a LTE/EPC, čímž vytvořil základ pro pokročilejší dočasné identifikátory, jako je P-TMSI v GPRS a GUTI v EPS. Řeší základní bezpečnostní požadavek ochrany identity, který je předpokladem pro důvěryhodné služby mobilní komunikace.

## Klíčové vlastnosti

- Dočasný, lokálně platný identifikátor nahrazující IMSI na rozhraní vzdušného přenosu
- Přidělen obsluhujícím síťovým uzlem (MSC/VLR nebo MME) po úspěšném ověření
- Používán ve všech rutinních signalizačních zprávách (např. odpověď na paging, aktualizace polohy)
- Zvyšuje soukromí účastníka a brání sledování
- Periodicky znovu přidělován pro zvýšení bezpečnosti
- Nezbytná součást mechanismu důvěrnosti identity sítě

## Související pojmy

- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [GUTI – Globally Unique Temporary UE Identity](/mobilnisite/slovnik/guti/)
- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [VLR – Visitor Location Register](/mobilnisite/slovnik/vlr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.022** (Rel-19) — ME Personalisation Features for GSM/3G
- **TR 22.944** (Rel-19) — UE Functionality Split Scenarios and Requirements
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.236** (Rel-19) — Intra Domain Connection of RAN Nodes to Multiple CN Nodes
- **TS 23.251** (Rel-19) — Network Sharing Stage 2 Specification
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.851** (Rel-6) — Network Sharing Architecture for 3G Systems
- **TR 23.923** (Rel-4) — Mobile IP+ Feasibility Study for UMTS/GPRS
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- … a dalších 14 specifikací

---

📖 **Anglický originál a plná specifikace:** [TMSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/tmsi/)
