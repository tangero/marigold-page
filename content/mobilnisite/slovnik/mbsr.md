---
slug: "mbsr"
url: "/mobilnisite/slovnik/mbsr/"
type: "slovnik"
title: "MBSR – Mobile Base Station Relay"
date: 2026-01-01
abbr: "MBSR"
fullName: "Mobile Base Station Relay"
category: "Radio Access Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mbsr/"
summary: "Síťový uzel, který funguje jako přenosová stanice (relay) s funkcionalitou základnové stanice a poskytuje bezdrátové páteřní připojení (backhaul). Typicky je integrován do pohyblivé platformy (např. v"
---

MBSR je mobilní přenosová stanice typu base station relay integrovaná do pohyblivé platformy, která zajišťuje bezdrátovou páteřní síť (backhaul) a dynamicky rozšiřuje pokrytí sítě.

## Popis

Mobile Base Station Relay (MBSR) je specializovaný síťový uzel definovaný v 3GPP, který kombinuje funkce přenosového uzlu (relay node) a základnové stanice (gNB nebo ng-eNB v 5G), ale odlišuje se svou vlastní mobilitou. Na rozdíl od pevných přenosových stanic je MBSR integrován do pohyblivého vozidla, jako je autobus, vlak, letadlo nebo bezpilotní systém (UAS/dron). Jeho primární úlohou je poskytovat bezdrátový přístup uživatelským zařízením (UE) v oblasti svého pokrytí, přičemž sám se připojuje k síti prostřednictvím bezdrátového páteřního spoje (wireless backhaul link) k dárkové základnové stanici (Donor gNB nebo DgNB). Tím vzniká dvouskoková architektura: bezdrátový páteřní spoj (mezi DgNB a MBSR) a přístupový spoj (mezi MBSR a UE).

Z architektonického hlediska MBSR hostuje plnou distribuovanou jednotku gNB (gNB-DU) a v závislosti na nasazení může hostovat i centralizovanou jednotku gNB (gNB-CU). K 5G jádru sítě (5G Core Network) se připojuje přes Donor gNB využitím rozhraní F1 přes bezdrátový páteřní spoj. MBSR spravuje vlastní buňku/buňky, vysílá vlastní Physical Cell ID a systémové informace. Pro uživatelská zařízení (UE), která obsluhuje, se jeví jako standardní základnová stanice. Klíčovou technickou výzvou je řízení mobility samotného MBSR, které zahrnuje procedury předávání hovoru (handover) pro celý přenosový uzel a s ním asociovaná UE, když se pohybuje mezi buňkami dárkových stanic.

Bezdrátový páteřní spoj může pracovat v pásmu (in-band, využívat stejné spektrum jako přístupový spoj) nebo mimo pásmo (out-of-band) a využívá pokročilé funkce jako principy integrovaného přístupu a páteře (IAB). MBSR musí zvládat dynamické změny topologie, možné zhoršení páteřního spoje v důsledku pohybu a být si vědom síťového řezování (network slicing), aby poskytoval konzistentní službu. Jeho provoz je koordinován sítí, která spravuje přidělování zdrojů pro páteřní i přístupové spoje, mobilitu a případně trajektorii MBSR v případě řízených platforem jako jsou drony.

## K čemu slouží

MBSR byl vytvořen, aby řešil potřebu flexibilního, na požádání dostupného a mobilního síťového pokrytí, které nelze ekonomicky efektivně zajistit pevnou infrastrukturou. Řeší problém poskytování nepřetržité kvalitní služby v pohyblivých vozidlech (vlacích, autobusech, lodích) a rychlého nasazení pokrytí pro dočasné události, obnovu po katastrofách nebo v odlehlých oblastech.

Překonává omezení tradičních řešení, jako je satelitní páteř (vysoká latence, náklady) nebo jednoduché opakovače typu UE-to-network (které nevytvářejí spravovanou buňku). Předchozí přístupy často vyžadovaly složitá nastavení směrovačů s více UE nebo neposkytovaly bezproblémový, do sítě integrovaný zážitek s podporou mobility, QoS a síťového řezování. MBSR jako standardizovaný 3GPP síťový uzel umožňuje operátorovi plně spravovat službu jako rozšíření vlastní RAN.

Motivace vychází z různých případů užití: poskytování vylepšené konektivity v hromadné dopravě, umožnění velení a řízení (command-and-control) pro pohyblivá hejna dronů, zajištění pokrytí pro první záchranáře v dynamických nouzových scénářích a podpora konektivity pro pohyblivá hotspotová místa na velkých akcích. Standardizací MBSR umožňuje 3GPP interoperabilní řešení pro tyto pokročilé scénáře mobilních přenosových stanic v rámci architektury 5G systému.

## Klíčové vlastnosti

- Plná funkcionalita základnové stanice (gNB/ng-eNB) hostovaná na mobilní platformě
- Bezdrátové páteřní připojení (wireless backhaul) k dárkové gNB, často využívající principy IAB
- Podpora mobility samotného přenosového uzlu, vyžadující předání (handover) MBSR a jím obsluhovaných UE
- Schopnost poskytovat spravované síťové pokrytí a kapacitu v dynamických, pohyblivých scénářích
- Podpora síťového řezování (network slicing), koncové QoS a zabezpečení přes přenosové spojení
- Integrace do architektury 5G systému pomocí standardizovaných rozhraní (např. F1 přes rádiové rozhraní)

## Definující specifikace

- **TS 23.273** (Rel-19) — 5G Location Services Stage 2 Architecture
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 28.875** (Rel-19) — Study on IAB Node Management
- **TS 29.515** (Rel-19) — Ngmlc Service Based Interface Protocol
- **TS 29.572** (Rel-19) — Nlmf Service Based Interface Stage 3

---

📖 **Anglický originál a plná specifikace:** [MBSR na 3GPP Explorer](https://3gpp-explorer.com/glossary/mbsr/)
