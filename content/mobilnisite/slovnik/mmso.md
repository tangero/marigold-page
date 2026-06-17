---
slug: "mmso"
url: "/mobilnisite/slovnik/mmso/"
type: "slovnik"
title: "MMSO – Multimedia Messaging Service Originator"
date: 2025-01-01
abbr: "MMSO"
fullName: "Multimedia Messaging Service Originator"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mmso/"
summary: "MMSO je funkční role v architektuře MMS představující entitu (typicky zařízení nebo aplikaci uživatele), která vytváří a odesílá multimediální zprávu k doručení. Iniciuje transakci MMS interakcí s MMS"
---

MMSO je funkční role v architektuře MMS pro entitu, například zařízení uživatele, která vytváří a odesílá multimediální zprávu.

## Popis

Multimedia Messaging Service Originator (MMSO) je logická role definovaná ve standardech [MMS](/mobilnisite/slovnik/mms/) 3GPP, která zahrnuje zdroj multimediální zprávy. V naprosté většině případů je MMSO implementována jako software (MMS User Agent) v mobilním zařízení účastníka, například ve smartphonu. Může jí však být i automatizovaná aplikace nebo server ve scénářích jako je zasílání zpráv typu application-to-person ([A2P](/mobilnisite/slovnik/a2p/)), například upozornění na zprávy nebo marketingové kampaně. Primární funkcí MMSO je sestavit multimediální zprávu – která může obsahovat text, obrázky, audio nebo video – a poté ji odeslat do síťového MMS Relay/Server (MMS-R/S) ke zpracování a doručení.

Technická operace začíná tím, že MMSO naváže datové spojení (např. přes [GPRS](/mobilnisite/slovnik/gprs/), UMTS nebo LTE). Poté použije rozhraní MM1, typicky přes [HTTP](/mobilnisite/slovnik/http/) nebo WAP, ke komunikaci s MMS-R/S. Proces odeslání zahrnuje zaslání zprávy MM1_submit.REQ. Tato zpráva je komplexní PDU (Protocol Data Unit), která obsahuje nejen samotný multimediální obsah (zakódovaný ve formátu [MIME](/mobilnisite/slovnik/mime/), jako je multipart/related), ale také klíčová metadata. Tato metadata zahrnují adresu(y) příjemce, adresu odesílatele, předmět, požadovaný čas doručení, čas expirace a indikaci, zda je vyžádána doručovací zpráva nebo zpráva o přečtení. MMSO je zodpovědná za správné naformátování této PDU podle specifikací 3GPP.

Po přijetí odpovědi MM1_submit.RES od MMS-R/S MMSO ví, že odeslání bylo přijato. MMSO může následně obdržet zprávu MM1_delivery_report.REQ, pokud ji vyžádala, která ji informuje o konečném stavu doručení do sítě příjemce. Role MMSO je odlišná od role MMS Recipient, ačkoli jediný MMS User Agent může plnit obě role. Specifikace řídící chování MMSO zajišťují, že všechny zdrojové přístroje a aplikace komunikují se sítí konzistentním způsobem, což je zásadní pro spolehlivý provoz služby, přesné účtování a předvídatelný uživatelský zážitek. Záznamy o účtování související se vznikem zprávy jsou často spouštěny na základě žádosti o odeslání od MMSO.

## K čemu slouží

Role MMSO byla formálně definována, aby vytvořila jasnou smluvní a funkční hranici v architektuře [MMS](/mobilnisite/slovnik/mms/). Identifikuje místo vzniku zprávy, což je klíčové z několika provozních a komerčních důvodů. Před takovou standardizací byl koncept 'odesílatele' nejednoznačný, zejména se zavedením automatizovaných služeb, což ztěžovalo účtování, řešení sporů a kontrolu spamu.

Její vytvoření řeší problém odpovědnosti a zodpovědnosti v toku zpráv. Přesným definováním MMSO standardy stanovují, která entita transakci iniciuje, kdo je odpovědný za obsah a formátování původního odeslání a která strana má být za vznik zprávy účtována. To je nezbytné pro generování přesných Charging Data Records ([CDR](/mobilnisite/slovnik/cdr/)) pro účely účtování. Dále umožňuje funkce jako doručovací zprávy vyžádané odesílatelem, protože MMSO je entita, která tuto potřebu signalizuje během odesílání. Role také usnadňuje vývoj služeb [A2P](/mobilnisite/slovnik/a2p/) tím, že poskytuje standardizovaný model pro servery, které vystupují jako původci, čímž rozšiřuje komerční případy užití MMS mimo komunikaci typu person-to-person.

## Klíčové vlastnosti

- Iniciuje transakci MMS odesláním zpráv do MMS Relay/Server
- Formátuje PDU MM1_submit.REQ s obsahem a metadaty (příjemci, předmět atd.)
- Může vyžádat doručovací zprávy a zprávy o přečtení pro odeslané zprávy
- Typicky implementována jako MMS User Agent v mobilním zařízení
- Může být také automatizovaný server pro zasílání zpráv typu Application-to-Person (A2P)
- Spouští vytvoření záznamů o účtování za vznik zprávy

## Související pojmy

- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)

## Definující specifikace

- **TS 32.270** (Rel-19) — MMS Charging Management Specification
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)

---

📖 **Anglický originál a plná specifikace:** [MMSO na 3GPP Explorer](https://3gpp-explorer.com/glossary/mmso/)
