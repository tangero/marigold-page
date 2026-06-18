---
slug: "mnrf-mme"
url: "/mobilnisite/slovnik/mnrf-mme/"
type: "slovnik"
title: "MNRF-MME – Mobile Not Reachable Flag in MME for SMS"
date: 2025-01-01
abbr: "MNRF-MME"
fullName: "Mobile Not Reachable Flag in MME for SMS"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mnrf-mme/"
summary: "Příznak nastavený v MME, když je UE nedosažitelné pro doručení SMS v EPS. Zabrání zbytečnému pagingu a signalizaci pro SMS, když je známo, že UE není dostupné, a optimalizuje tak síťové zdroje."
---

MNRF-MME je příznak nastavený v MME, když je UE nedosažitelné pro doručení SMS v EPS, čímž se zabrání zbytečnému pagingu a signalizaci za účelem optimalizace síťových zdrojů.

## Popis

Mobile Not Reachable Flag in [MME](/mobilnisite/slovnik/mme/) for [SMS](/mobilnisite/slovnik/sms/) (MNRF-MME) je mechanismus správy mobility specifický pro Evolved Packet System (EPS) definovaný v 3GPP TS 23.272. Jedná se o binární příznak udržovaný v rámci Mobility Management Entity (MME) pro konkrétní User Equipment (UE). Tento příznak je nastaven, když MME zjistí, že UE není dosažitelné pro pokusy o doručení služby Short Message Service (SMS), typicky přes rozhraní SGs, které spojuje MME s [MSC](/mobilnisite/slovnik/msc/) pro procedury Circuit-Switched ([CS](/mobilnisite/slovnik/cs/)) fallback včetně SMS.

Když má být SMS doručena do UE, [SMS-SC](/mobilnisite/slovnik/sms-sc/) ji směruje přes MSC, které následně dotazuje MME přes rozhraní SGs. Pokud je pro dané UE nastaven příznak MNRF-MME, může MME okamžitě informovat MSC, že UE není dosažitelné, namísto zahájení procedury pagingu. Toto rozhodnutí je učiněno na základě stavu správy mobility UE; například pokud je UE v nedosažitelném stavu, jako je EMM-DEREGISTERED z důvodu vypršení časovače implicitního odpojení (implicit detach) nebo odpojení iniciovaného sítí, je příznak nastaven. MME také nastaví tento příznak, pokud předchozí pokus o paging pro SMS selhal.

Hlavní úlohou MNRF-MME je fungovat jako mezipaměť stavu dosažitelnosti uvnitř jádra sítě, aby se zabránilo marným pokusům o paging. Je úzce integrován s procedurami rozhraní SGs a stavovým automatem EPS Mobility Management ([EMM](/mobilnisite/slovnik/emm/)) UE. Příznak je vymazán, když UE úspěšně provede proceduru Tracking Area Update ([TAU](/mobilnisite/slovnik/tau/)), Service Request nebo Attach, čímž signalizuje, že je opět v dosažitelném stavu. Tento mechanismus je klíčový pro efektivní doručování SMS v sítích LTE/EPC, kde je SMS často zpracováváno přes CS fallback, zajišťuje, že síťové zdroje nejsou plýtvány na paging nedosažitelných zařízení, a umožňuje vhodné zpracování v SMS Service Centre.

## K čemu slouží

MNRF-MME byl zaveden za účelem optimalizace doručování [SMS](/mobilnisite/slovnik/sms/) a využití síťových zdrojů v sítích LTE. Před LTE bylo SMS v sítích GSM/UMTS doručováno přes CS doménu a dosažitelnost spravovala MSC/VLR. S příchodem plně IP EPS vyžadovalo doručování SMS pro UE bez schopnosti CS fallback nové mechanismy, jako je SMS over IP (SMS in MME), ale pro UE používající CS fallback SMS (SMS over SGs) byla potřeba metoda, která by zabránila MME v opakovaném pagingu UE známého jako nedosažitelného.

Bez MNRF-MME by každý pokus o SMS pro nedosažitelné UE spustil plnou proceduru pagingu napříč LTE rádiovou přístupovou sítí, což by zbytečně spotřebovávalo cenné zdroje rádiové a jádrové síťové signalizace. Tento příznak poskytuje paměťovou funkci uvnitř MME, která mu umožňuje zkrátit proces a okamžitě odpovědět MSC indikací selhání. Tím se snižuje signalizační zátěž, zlepšuje se celková efektivita sítě a poskytuje se rychlejší zpětná vazba pro SMS-SC, které pak mohou podniknout vhodné kroky, jako je uložení zprávy pro pozdější doručení. Řeší specifickou provozní neefektivitu, která vznikla v rozdělené architektuře EPS, kde byla správa mobility pro SMS zpracovávána odděleně přes rozhraní SGs.

## Klíčové vlastnosti

- Binární příznak udržovaný pro každé UE v MME
- Specifický pro doručování SMS přes rozhraní SGs pro CS fallback
- Zabraňuje zbytečným procedurám pagingu pro nedosažitelná UE
- Nastaven na základě stavu EMM UE (např. implicitní odpojení) nebo selhání pagingu
- Vymazán po úspěšných procedurách mobility nebo připojení UE (TAU, Attach)
- Integrován se stavovým automatem EPS Mobility Management (EMM)

## Související pojmy

- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [CSFB – Circuit Switched Fallback](/mobilnisite/slovnik/csfb/)

## Definující specifikace

- **TS 23.272** (Rel-19) — CS Fallback in EPS

---

📖 **Anglický originál a plná specifikace:** [MNRF-MME na 3GPP Explorer](https://3gpp-explorer.com/glossary/mnrf-mme/)
