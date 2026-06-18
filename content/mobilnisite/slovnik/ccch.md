---
slug: "ccch"
url: "/mobilnisite/slovnik/ccch/"
type: "slovnik"
title: "CCCH – Common Control Channel"
date: 2025-01-01
abbr: "CCCH"
fullName: "Common Control Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ccch/"
summary: "Logický kanál používaný pro přenos řídicích informací mezi sítí a mobilními zařízeními před navázáním vyhrazených spojení. Zpracovává počáteční přístupové procedury, jako je náhodný přístup, vyvoláván"
---

CCCH je logický kanál používaný pro přenos řídicích informací mezi sítí a mobilními zařízeními za účelem zpracování počátečních přístupových procedur, jako je náhodný přístup, vyvolávání a vysílání systémových informací.

## Popis

Common Control Channel (CCCH) je základní logický kanál v 3GPP rádiových přístupových sítích ([UTRAN](/mobilnisite/slovnik/utran/), [E-UTRAN](/mobilnisite/slovnik/e-utran/) a NR), který funguje ve směru uplink i downlink. Jako řídicí kanál nepřenáší uživatelská data, ale je nezbytný pro počáteční signalizační procedury, které umožňují uživatelskému zařízení (UE) přístup k síti. CCCH se používá, když mezi UE a sítí neexistuje spojení řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)), nebo když je UE ve stavu RRC_IDLE a potřebuje zahájit komunikaci. Funguje na sdílených rádiových zdrojích a je mapován na transportní kanály, jako je Random Access Channel ([RACH](/mobilnisite/slovnik/rach/)) ve směru uplink a Forward Access Channel ([FACH](/mobilnisite/slovnik/fach/)) v UMTS nebo Downlink Shared Channel ([DL-SCH](/mobilnisite/slovnik/dl-sch/)) v LTE/NR pro downlink.

Ve směru uplink používá CCCH primárně UE k odesílání počátečních přístupových zpráv. Nejzásadnější procedurou je RRC Connection Request, kdy UE zahajuje připojení k síti odesláním své identity (např. Temporary Mobile Subscriber Identity – [TMSI](/mobilnisite/slovnik/tmsi/) nebo náhodné hodnoty) a důvodu pro zřízení (např. volání iniciované mobilem, nouzové volání nebo aktualizace oblasti sledování). Tato zpráva je přenášena poté, co UE úspěšně dokončí proceduru náhodného přístupu na fyzické vrstvě na [PRACH](/mobilnisite/slovnik/prach/). Zpráva uplink CCCH je přenášena přes transportní kanál RACH v UMTS nebo UL-SCH v LTE/NR po úspěšném konkurenčním předpisu náhodného přístupu.

Ve směru downlink používá síť CCCH k reakci na pokusy o přístup ze strany UE a k vysílání základních systémových informací. Klíčovou downlink zprávou je RRC Connection Setup, což je odpověď sítě na úspěšný RRC Connection Request. Tato zpráva obsahuje počáteční konfiguraci rádiových zdrojů pro UE a nařizuje mu přejít do stavu RRC_CONNECTED a přepnout na používání vyhrazených řídicích kanálů (DCCH). Downlink CCCH se také používá pro přenos zpráv RRC Connection Reject, když síť nemůže vyhovět žádosti. Dále jsou bloky systémových informací (SIBs), které obsahují kritické parametry pro výběr buňky, řízení přístupu a informace o sousedních buňkách, vysílány na logickém kanálu BCCH, ale plánovací informace pro tyto SIBy jsou často signalizovány pomocí řídicích informací spojených s přidělováním sdílených zdrojů CCCH.

Architektura zpracování CCCH zahrnuje více protokolových vrstev. Na vrstvě RRC je CCCH přístupovým bodem služby (SAP) pro řídicí zprávy. Tyto zprávy jsou následně zpracovávány vrstvou Packet Data Convergence Protocol (PDCP) pro ochranu integrity (v NR) a vrstvou Radio Link Control (RLC), která pro zprávy CCCH funguje v transparentním režimu (TM), což znamená, že nepřidává hlavičku. Vrstva Medium Access Control (MAC) je zodpovědná za multiplexování logických kanálů (včetně CCCH) na transportní kanály a za zpracování plánování a procesů HARQ pro sdílené zdroje. Fyzická vrstva následně mapuje tyto transportní kanály na fyzické kanály pro přenos přes rádiové rozhraní. Role CCCH je přechodná, ale klíčová; jakmile je RRC spojení navázáno, veškerá následná signalizace přechází na Dedicated Control Channel (DCCH), který pro spolehlivé doručení používá potvrzovaný režim RLC.

## K čemu slouží

CCCH byl vytvořen, aby řešil základní problém počátečního přístupu k síti v celulárním systému. Před přidělením jakýchkoli vyhrazených zdrojů musí mít mobilní zařízení standardizovanou, efektivní metodu, jak kontaktovat síť, identifikovat se a požádat o službu. CCCH poskytuje tento sdílený, konkurenční signalizační kanál, který umožňuje jakémukoli zařízení v buňce zahájit komunikaci bez předem navázaného kontextu. Je vstupním bodem pro všechny síťové služby, od hlasových hovorů po datové relace.

Historicky měly rané celulární systémy jako GSM také společné řídicí kanály (jako RACH a AGCH) a koncept 3GPP CCCH se z těchto principů vyvinul do architektur UMTS a později LTE/5G NR. Řeší omezení spočívající pouze ve vyhrazených kanálech tím, že poskytuje škálovatelnou a zdrojově efektivní metodu pro zpracování sporadických pokusů o přístup z potenciálně tisíců nečinných zařízení. Bez společného kanálu by síť musela trvale přidělovat vyhrazené zdroje každému zařízení, což je z hlediska řízení rádiových zdrojů nemožné. CCCH umožňuje model komunikace mnoha-ku-jednomu pro počáteční přístup, což je nezbytné pro škálovatelnost sítě a energetickou účinnost baterií v mobilních zařízeních, protože ta potřebují aktivovat své vysílače pouze na krátkou dobu k odeslání přístupové žádosti.

CCCH je navíc klíčový pro řízenou mobilitu a dosažitelnost v síti. Prostřednictvím přidruženého kanálu pro vyvolávání (který je technicky na logickém kanálu PCCH, ale spoléhá se na strukturu řídicí roviny zahrnující CCCH) může síť lokalizovat a upozornit nečinná UE na příchozí hovory nebo data. Počáteční odpověď vyvolaného UE také využívá uplink CCCH. CCCH tedy řeší dvojí problém počátečního připojení k síti a efektivní dosažitelnosti zařízení a tvoří základ architektury řídicí roviny ve všech 3GPP rádiových přístupových technologiích.

## Klíčové vlastnosti

- Poskytuje počáteční signalizaci uplink pro zřízení RRC spojení (RRC Connection Request)
- Přenáší downlink odpovědi sítě, jako jsou RRC Connection Setup a RRC Connection Reject
- Funguje, když neexistuje RRC spojení, a využívá sdílené/konkurenční zdroje
- Využívá transparentní režim RLC pro doručování zpráv s nízkou latencí
- Je mapován na transportní kanály, jako je RACH (UL) a FACH/DL-SCH (DL), v závislosti na RAT
- Nezbytný pro procedury výběru buňky, získávání systémových informací a odpovědi na vyvolávání

## Související pojmy

- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)
- [DCCH – Dedicated Control Channel](/mobilnisite/slovnik/dcch/)
- [RACH – Random Access Channel](/mobilnisite/slovnik/rach/)
- [BCCH – Broadcast Control Channel](/mobilnisite/slovnik/bcch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- **TS 34.124** (Rel-19) — EMC Requirements for 3G UTRA Terminals
- **TS 36.124** (Rel-19) — EMC for E-UTRA User Equipment
- **TS 36.133** (Rel-19) — E-UTRA RRM Requirements
- **TS 36.322** (Rel-19) — E-UTRA Radio Link Control Protocol Specification
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- … a dalších 5 specifikací

---

📖 **Anglický originál a plná specifikace:** [CCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/ccch/)
