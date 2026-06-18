---
slug: "rslpp"
url: "/mobilnisite/slovnik/rslpp/"
type: "slovnik"
title: "RSLPP – Ranging and Sidelink Positioning Policy"
date: 2026-01-01
abbr: "RSLPP"
fullName: "Ranging and Sidelink Positioning Policy"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/rslpp/"
summary: "Rámec politiky zavedený v 3GPP Release 18 pro správu a autorizaci služeb měření vzdálenosti a určování polohy využívajících komunikaci mezi zařízeními přes postranní spoj (sidelink). Umožňuje zabezpeč"
---

RSLPP je rámec politiky (policy framework) 3GPP Release 18, který autorizuje a spravuje zabezpečené služby měření vzdálenosti (ranging) a určování polohy využívající přímou komunikaci mezi zařízeními přes postranní spoj (sidelink).

## Popis

RSLPP (Ranging and Sidelink Positioning Policy) je rámec pro řízení politik definovaný v rámci 5G systému (5GS) za účelem regulace využívání služeb měření vzdálenosti a určování polohy založených na postranním spoji (sidelink). Postranní spoj označuje přímou komunikaci mezi zařízeními (device-to-device), která obchází síťovou infrastrukturu, a je využívána v technologiích jako NR Sidelink ([SL](/mobilnisite/slovnik/sl/)) pro komunikaci Vozidlo-se-vším ([V2X](/mobilnisite/slovnik/v2x/)) a scénáře veřejné bezpečnosti. RSLPP poskytuje pravidla a autorizační mechanismy, které určují, kdy, jak a za jakých podmínek mohou dvě nebo více uživatelských zařízení (UE) provádět měření vzdálenosti (ranging) nebo spolupracující určování polohy (collaborative positioning) s využitím prostředků postranního spoje.

Z architektonického hlediska je RSLPP spravován funkcí pro řízení politik (Policy Control Function – [PCF](/mobilnisite/slovnik/pcf/)), což je entita jádra sítě zodpovědná za řízení politik a účtování. PCF generuje politiky RSLPP na základě profilů účastníků, požadavků služeb a stavu sítě. Tyto politiky jsou následně poskytovány příslušným uživatelským zařízením (UE) prostřednictvím funkce pro správu přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) nebo přímo přes řídicí kanály postranního spoje. Samotná politika obsahuje parametry, jako jsou autorizovaná partnerská zařízení, povolené metody měření vzdálenosti (např. Time-of-Arrival, Round-Trip-Time), povolená frekvence a doba trvání relací měření, geografické oblasti, kde je měření povoleno, a požadované bezpečnostní přihlašovací údaje.

Operačně, když má uživatelské zařízení (UE) v úmyslu zahájit relaci měření vzdálenosti s jiným UE, musí nejprve vyhodnotit lokálně uloženou politiku RSLPP. Politika určuje, zda je požadavek povolen. Pokud je autorizován, uživatelské zařízení použije signalizaci přes postranní spoj (např. prostřednictvím Sidelink Control Information – [SCI](/mobilnisite/slovnik/sci/)) ke koordinaci procedury měření s partnerským UE. Samotné měření vzdálenosti může využívat signály fyzické vrstvy, jako jsou Positioning Reference Signals ([PRS](/mobilnisite/slovnik/prs/)) vysílané přes postranní spoj. Výsledky mohou být zpracovány lokálně nebo nahlášeny zpět funkci pro správu polohy ([LMF](/mobilnisite/slovnik/lmf/)) pro zvýšení přesnosti. RSLPP zajišťuje, že tyto operace nezasahují do ostatního provozu na postranním spoji, dodržují regulační omezení (např. ohledně soukromí) a efektivně využívají prostředky.

Její role v síti je klíčová pro umožnění pokročilých služeb založených na poloze v decentralizovaných scénářích. V komunikaci V2X mohou vozidla přesně určovat vzájemné polohy pro zabránění kolizím bez neustálé závislosti na [GNSS](/mobilnisite/slovnik/gnss/). Ve službách veřejné bezpečnosti mohou záchranáři lokalizovat členy týmu v prostředích se špatnou viditelností. RSLPP poskytuje nezbytný rámec správy, aby byly tyto služby spolehlivé, škálovatelné a zabezpečené v rámci architektury politik 5G, a integruje tak možnosti postranního spoje do širší architektury síťových služeb.

## K čemu slouží

RSLPP byl vytvořen, aby řešil rostoucí potřebu přesného relativního určování polohy mezi zařízeními v scénářích přímé komunikace, zejména v rámci ekosystémů 5G V2X a IoT. Před Release 18 komunikace přes postranní spoj (zavedená pro výměnu dat v Rel-16/17) postrádala standardizovaný mechanismus politiky pro koordinaci aktivit určování polohy. Zařízení mohla provádět ad-hoc měření vzdálenosti, což však vedlo k potenciálním problémům: nekoordinované využívání mohlo zahlcovat prostředky postranního spoje, měření mohla být nespolehlivá bez dohodnutých protokolů a neexistovaly formální autorizační kontroly, což vyvolávalo obavy o bezpečnost a soukromí.

Motivace vychází z vývoje 5G směrem k podpoře pokročilých spolupracujících aplikací. Formování kolon vozidel, koordinace rojů dronů a interakce ve rozšířené realitě vyžadují, aby zařízení znala svou vzájemnou polohu s vysokou přesností a nízkou latencí. Zatímco GNSS poskytuje absolutní polohu, často je nedostatečná v městských kaňonech, v interiérech nebo pro přesné relativní měření vzdálenosti. Měření vzdálenosti založené na postranním spoji nabízí doplňkovou, přímou metodu měření. Bez rámce politiky však takové služby nemohly být provozovateli sítí spolehlivě spravovány nebo zpoplatňovány. RSLPP poskytuje tuto vrstvu správy, což operátorům umožňuje řídit a nabízet měření vzdálenosti jako certifikovanou službu.

Řeší problém integrace ad-hoc, na zařízení orientovaného určování polohy do architektury řízení politik a účtování 5G spravované operátorem. Definováním formální politiky zajišťuje, že služby měření vzdálenosti jsou poskytovány pouze autorizovaným účastníkům, v autorizovaných kontextech a s využitím autorizovaných metod. Tím se předchází zneužití, optimalizuje se využití rádiových prostředků a umožňuje se diferenciace služeb. Usnadňuje také dodržování regionálních předpisů týkajících se soukromí polohových údajů. RSLPP tak překlenuje propast mezi decentralizovanými operacemi na postranním spoji a centralizovaným síťovým řízením politik, což umožňuje škálovatelné, komerčně využitelné služby měření vzdálenosti a určování polohy.

## Klíčové vlastnosti

- Autorizace relací měření vzdálenosti a určování polohy na postranním spoji založená na politice
- Definuje povolené metody měření vzdálenosti (např. ToA, RTT) a konfigurace signálů
- Specifikuje geografická a časová omezení pro aktivity měření vzdálenosti
- Integruje se s funkcí pro řízení politik 5G (PCF) pro centralizovanou správu
- Podporuje diferenciaci politik specifických pro uživatelské zařízení (UE) a pro službu
- Umožňuje zabezpečenou výměnu přihlašovacích údajů pro ověřené procedury měření vzdálenosti

## Související pojmy

- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)

## Definující specifikace

- **TS 23.503** (Rel-20) — 5G Policy and Charging Control Framework
- **TS 24.514** (Rel-19) — Ranging & Sidelink Positioning in 5GS
- **TS 24.526** (Rel-19) — UE Policies for 5GS; Stage 3
- **TS 24.587** (Rel-19) — V2X Services Protocols for 5G System
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- **TS 29.525** (Rel-19) — 5G UE Policy Control Service Stage 3

---

📖 **Anglický originál a plná specifikace:** [RSLPP na 3GPP Explorer](https://3gpp-explorer.com/glossary/rslpp/)
