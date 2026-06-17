---
slug: "ber"
url: "/mobilnisite/slovnik/ber/"
type: "slovnik"
title: "BER – Basic Encoding Rules"
date: 2026-01-01
abbr: "BER"
fullName: "Basic Encoding Rules"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ber/"
summary: "BER je sada standardizovaných pravidel pro kódování datových struktur definovaných v ASN.1 (Abstract Syntax Notation One) do serializovaného binárního proudu. Jedná se o základní kódovací schéma hojně"
---

BER je standardizovaná sada pravidel pro kódování datových struktur definovaných v ASN.1 do binárního proudu, která je hojně používána v signalizačních protokolech 3GPP pro zajištění jednoznačné výměny dat mezi síťovými prvky.

## Popis

Basic Encoding Rules (BER) je metoda pro kódování datových objektů popsaných v jazyce Abstract Syntax Notation One (ASN.1) do řetězce oktetů (bytů). ASN.1 je standardní jazyk pro popis rozhraní používaný k definování struktury protokolových datových jednotek (PDU) způsobem nezávislým na platformě. BER poskytuje konkrétní překlad z této abstraktní definice do konkrétní reprezentace na úrovni bitů, která může být přenášena po síti nebo uložena. Jedná se o kódovací schéma typu tag-délka-hodnota (TLV), díky čemuž jsou zakódovaná data samoopisná.

Z architektonického hlediska BER pracuje s jednotlivými typy ASN.1. Proces kódování jakéhokoli datového prvku vytváří tři po sobě jdoucí pole: oktety identifikátoru (tag), oktety délky a oktety obsahu (hodnoty). Tag identifikuje typ dat (např. INTEGER, SEQUENCE, OCTET STRING) a to, zda jsou primitivní nebo konstruovaná. Pole Délka určuje počet oktetů v poli Obsah. Pole Obsah obsahuje skutečnou zakódovanou hodnotu dat. U jednoduchých typů, jako je INTEGER, je hodnota zakódována přímo. U konstruovaných typů, jako je SEQUENCE nebo SET, obsahuje pole Obsah zřetězená BER kódování každé komponentní části.

Jak to funguje, zahrnuje rekurzivní proces. Kodér prochází datovou strukturu ASN.1 a aplikuje pravidlo TLV na každý uzel. Klíčovou vlastností je jeho flexibilita; BER nabízí pro některé datové typy více kódovacích forem (např. formy s určitou a neurčitou délkou). V 3GPP je BER specifikována jako přenosová syntax pro četné signalizační protokoly vrstvy 3, zejména v jádru sítě. Například protokoly jako Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)), Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)) a mnoho aplikačních protokolů v jádru (často používajících variantu ASN.1 PER) mají své kořeny v principech kódování BER. Jejím úkolem je zajistit, aby zpráva vygenerovaná zařízením jednoho výrobce mohla být správně parsována a pochopena zařízením jiného výrobce, čímž poskytuje základní interoperabilitu pro vícevýrobcové telekomunikační sítě.

## K čemu slouží

BER existuje, aby řešila základní problém heterogenní reprezentace dat v distribuovaných systémech a telekomunikačních sítích. Různé počítačové architektury reprezentují data různými způsoby (např. pořadí bajtů, velikost celých čísel). Bez společného, jednoznačného kódovacího pravidla by se dva systémy mohly shodnout na abstraktní struktuře zprávy (prostřednictvím ASN.1), ale stále by nedokázaly správně vyměňovat data kvůli rozdílům v nízkonákladové reprezentaci. BER poskytuje kanonickou, externí reprezentaci, která je nezávislá na jakýchkoli podrobnostech specifických pro daný stroj.

Její vytvoření bylo motivováno potřebou robustních, interoperabilních specifikací protokolů v počátcích digitální telekomunikace a datových sítí (model [OSI](/mobilnisite/slovnik/osi/)). Před takovými standardy byly specifikace protokolů často nejednoznačné, což vedlo k nákladným a časově náročným problémům s integrací. BER ve spojení s ASN.1 umožňuje návrhářům protokolů přesně definovat složité, vnořené datové struktury a poskytuje standardizovaný způsob jejich serializace. To dramaticky snižuje chyby implementace a zajišťuje, že síťové prvky od různých výrobců mohou bezproblémově komunikovat, což je základním principem veřejných standardů, jako jsou ty od 3GPP. Řeší tak omezení ad-hoc nebo proprietárních kódovacích schémat, která uzamkla sítě do řešení od jediného dodavatele.

## Klíčové vlastnosti

- Definuje strukturu Tag-Délka-Hodnota (TLV) pro kódování datových typů ASN.1
- Poskytuje samoopisná data, protože tag identifikuje typ zakódované hodnoty
- Podporuje jak primitivní (jednoduché), tak konstruované (složené) formy kódování
- Umožňuje metody kódování s určitou délkou a s neurčitou délkou
- Zajišťuje výměnu dat nezávislou na platformě mezi síťovými entitami
- Tvoří základ pro další kódovací pravidla ASN.1, jako jsou CER, DER a PER

## Související pojmy

- [DER – Distinguished Encoding Rules](/mobilnisite/slovnik/der/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.101** (Rel-20) — Service Principles for PLMNs
- **TS 22.105** (Rel-19) — Telecommunication Services Framework
- **TR 22.925** (Rel-4) — UMTS QoS and Network Performance Parameters
- **TS 23.050** (R99) — UMTS Network Principles and Architecture
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TR 23.979** (Rel-19) — PoC over 3GPP Systems Architectural Requirements
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.105** (Rel-19) — UTRA TDD Base Station RF Requirements
- **TS 25.111** (Rel-19) — LMU RF Characteristics for UTRA FDD
- … a dalších 39 specifikací

---

📖 **Anglický originál a plná specifikace:** [BER na 3GPP Explorer](https://3gpp-explorer.com/glossary/ber/)
