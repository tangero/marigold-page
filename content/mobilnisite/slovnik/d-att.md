---
slug: "d-att"
url: "/mobilnisite/slovnik/d-att/"
type: "slovnik"
title: "D-ATT – Downlink Attach"
date: 2025-01-01
abbr: "D-ATT"
fullName: "Downlink Attach"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/d-att/"
summary: "D-ATT je procedura v sítích GSM/UMTS, při které síť iniciuje navázání spojení s mobilním zařízením ve směru downlink. Jedná se o klíčový mechanismus pro umožnění služeb iniciovaných sítí, jako jsou hl"
---

D-ATT je procedura v sítích GSM/UMTS iniciovaná sítí (downlink) pro navázání spojení s mobilním zařízením, která umožňuje služby iniciované sítí, jako jsou hlasové hovory a SMS.

## Popis

Downlink Attach (D-ATT) je procedura iniciovaná sítí, definovaná v okruhově komutované ([CS](/mobilnisite/slovnik/cs/)) doméně GSM a UMTS, konkrétně pro navázání downlink spojení s mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)). Procedura je spuštěna, když síť potřebuje doručit službu iniciovanou sítí, jako je příchozí hlasový hovor nebo SMS zpráva, účastníkovi. Hlavním cílem je lokalizovat zařízení účastníka, navázat rádiové spojení a připravit potřebné zdroje pro doručení služby.

Proceduru D-ATT řídí prvky jádra sítě, především Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) a Visitor Location Register (VLR). Když dorazí požadavek na službu iniciovanou sítí, MSC/VLR zahájí D-ATT odesláním zprávy paging request do Base Station Subsystem ([BSS](/mobilnisite/slovnik/bss/)) v GSM nebo Radio Network Subsystem (RNS) v UMTS. Tento paging request obsahuje Temporary Mobile Subscriber Identity (TMSI) nebo International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)) účastníka k identifikaci cílového zařízení. BSS/RNS následně vysílá paging zprávu v příslušné lokalizační oblasti ([LA](/mobilnisite/slovnik/la/)) nebo směrovací oblasti (RA).

Po přijetí paging zprávy cílové MS odpoví channel request, čímž iniciuje proceduru náhodného přístupu (random access) ve směru uplink. Síť následně přiřadí MS vyhrazený traffic kanál (TCH) nebo signalizační kanál (SDCCH). Po tomto přiřazení kanálu odešle MS zprávu paging response zpět k MSC/VLR přes BSS/RNS, čímž potvrdí svou dostupnost a polohu. Tato odpověď umožní MSC/VLR autentizovat účastníka, v případě potřeby provést šifrování a pokračovat ve zřízení hovoru nebo relace.

Procedura D-ATT je kritickou součástí protokolů pro správu mobility a řízení hovorů. Zajišťuje, že síť může spolehlivě dosáhnout účastníka, i když je zařízení v idle módu, a to využitím mechanismů sledování lokalizačních oblastí. Efektivita a spolehlivost D-ATT přímo ovlivňuje klíčové výkonnostní ukazatele, jako je úspěšnost zřízení hovoru a doba odezvy na paging, což z ní činí životně důležitý proces pro síťové operátory.

## K čemu slouží

Procedura D-ATT byla vytvořena, aby vyřešila základní problém komunikace iniciované sítí v celulárních sítích. Před standardizovanými celulárními systémy vyžadovalo dosažení mobilního uživatele manuální asistenci operátora nebo předem dohodnuté kanály. D-ATT poskytuje automatizovanou, standardizovanou metodu, kterou síť lokalizuje a naváže spojení s mobilním zařízením v idle stavu, čímž umožňuje všudypřítomné služby iniciované sítí.

Její vytvoření bylo motivováno potřebou efektivní dosažitelnosti účastníka v rámci architektury GSM zavedené v 80. letech. Procedura umožňuje síti šetřit rádiové zdroje tím, že udržuje zařízení v idle módu, když aktivně nekomunikují, a přitom si zachovává schopnost kontakt iniciovat. Řeší omezení spočívající v neexistenci trvalého spojení s každým zařízením, které by bylo náročné na zdroje, tím, že využívá paging mechanismus k upozornění konkrétních zařízení pouze v případě potřeby.

D-ATT je nezbytná pro komerční životaschopnost mobilní telefonie, protože umožňuje základní službu přijímání příchozích hovorů. Tvoří páteř všech okruhově komutovaných služeb iniciovaných sítí a zajišťuje, že účastníci jsou dosažitelní kdekoli v oblasti pokrytí sítě. Návrh procedury v rámci GSM Rel-8 a její pokračování v pozdějších vydáních 3GPP podtrhuje její trvalou roli jako základní funkce správy mobility.

## Klíčové vlastnosti

- Navázání spojení iniciované sítí pro služby iniciované sítí (mobile-terminated)
- Využívá paging v lokalizační oblasti (LA) nebo směrovací oblasti (RA) k nalezení zařízení v idle stavu
- Zahrnuje prvky jádra sítě MSC a VLR pro koordinaci procedury
- Spouští náhodný přístup (random access) a přiřazení vyhrazeného kanálu na rádiovém rozhraní
- Umožňuje autentizaci účastníka a šifrování během zřizování spojení
- Základní pro ukazatele úspěšnosti doručení hovoru a dosažitelnosti účastníka (KPI)

## Definující specifikace

- **TS 43.068** (Rel-19) — Voice Group Call Service (VGCS) Stage 2

---

📖 **Anglický originál a plná specifikace:** [D-ATT na 3GPP Explorer](https://3gpp-explorer.com/glossary/d-att/)
