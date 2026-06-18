---
slug: "sl-prs-cs-rnti"
url: "/mobilnisite/slovnik/sl-prs-cs-rnti/"
type: "slovnik"
title: "SL-PRS-CS-RNTI – Sidelink Positioning Reference Signal Configured Scheduling Radio Network Temporary Identifier"
date: 2025-01-01
abbr: "SL-PRS-CS-RNTI"
fullName: "Sidelink Positioning Reference Signal Configured Scheduling Radio Network Temporary Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sl-prs-cs-rnti/"
summary: "Jedinečný identifikátor přiřazený uživatelskému zařízení (UE) pro příjem konfigurovaných plánovacích povolení pro vysílání referenčních signálů pro pozicování na postranním spoji (SL-PRS). Umožňuje ef"
---

SL-PRS-CS-RNTI je jedinečný identifikátor přiřazený uživatelskému zařízení (UE) pro příjem konfigurovaných plánovacích povolení (configured scheduling grants) pro vysílání referenčních signálů pro pozicování na postranním spoji (Sidelink Positioning Reference Signal), což umožňuje efektivní přidělování zdrojů pro pozicování na postranním spoji.

## Popis

SL-PRS-CS-RNTI je specifický typ dočasného identifikátoru rádiové sítě ([RNTI](/mobilnisite/slovnik/rnti/)) definovaného v rámci 3GPP NR postranního spoje, jak je podrobně popsáno ve specifikaci 38.321. Funguje jako uživatelskému zařízení specifický identifikátor používaný v řídicí informaci na downlinku ([DCI](/mobilnisite/slovnik/dci/)) k aktivaci, deaktivaci nebo modifikaci konfigurovaných povolení pro vysílání referenčních signálů pro pozicování na postranním spoji ([SL-PRS](/mobilnisite/slovnik/sl-prs/)). Tato konfigurovaná povolení jsou polotrvalá plánovací přiřazení, která umožňují periodické vysílání SL-PRS bez nutnosti dynamického povolení pro každý přenos, čímž se snižuje režie řídicí signalizace a latence.

Z architektonického hlediska SL-PRS-CS-RNTI funguje v rámci vrstvy řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) uživatelského zařízení. gNB nebo plánující UE používá tento RNTI ke skramblování kontrolního součtu cyklické redundance ([CRC](/mobilnisite/slovnik/crc/)) DCI formátu 3_0, který nese informace o povolení pro postranní spoj. Když UE detekuje DCI s CRC skramblovaným pomocí jí přiřazeného SL-PRS-CS-RNTI, interpretuje parametry povolení a aplikuje je do své konfigurace pro vysílání SL-PRS. Tento proces je nedílnou součástí operace konfigurovaného povolení typu 1, kde je povolení poskytnuto prostřednictvím [RRC](/mobilnisite/slovnik/rrc/) signalizace a aktivováno DCI, nebo typu 2, kde je povolení poskytnuto a aktivováno výhradně prostřednictvím DCI.

Klíčové komponenty zahrnují samotnou hodnotu RNTI, DCI formát 3_0 a přidruženou konfiguraci zdrojů SL-PRS. Úlohou SL-PRS-CS-RNTI je poskytnout cílený mechanismus pro plánování zdrojů postranního spoje specifických pro pozicování. Zajišťuje, že pouze zamýšlená uživatelská zařízení dekódují a jednají podle plánovacích příkazů, čímž udržují efektivní využití rádiových zdrojů a podporují spolehlivý přenos pozicovacích signálů, což je základním předpokladem pro pokročilé služby postranního spoje, jako je relativní pozicování, měření vzdálenosti a kooperativní vnímání ve vozidlových a průmyslových IoT scénářích.

## K čemu slouží

SL-PRS-CS-RNTI bylo zavedeno v 3GPP Release 18, aby řešilo potřebu efektivního a spolehlivého plánování referenčních signálů pro pozicování v komunikaci na postranním spoji. Před jeho zavedením se pozicování na postranním spoji spoléhalo na obecnější plánovací mechanismy nebo na zdroje přidělované na základě soutěžení, což mohlo vést k nepředvídatelné latenci, kolizím a nedostatečné spolehlivosti pro časově citlivé pozicovací aplikace, jako je autonomní řízení nebo koordinace dronů.

Jeho vytvoření bylo motivováno vývojem [V2X](/mobilnisite/slovnik/v2x/) a služeb blízkosti ([ProSe](/mobilnisite/slovnik/prose/)) směrem k náročnějším případům užití vyžadujícím přesnost pozicování na úrovni pod metr. Mezi omezení předchozích přístupů patřila vysoká režie signalizace z dynamických povolení pro periodické pozicovací signály a absence vyhrazeného řízení pro přenosy specifické pro pozicování. Díky umožnění konfigurovaného plánování pro SL-PRS SL-PRS-CS-RNTI snižuje zahlcení řídicího kanálu, zajišťuje včasné a periodické vysílání pozicovacích signálů a zlepšuje celkovou kapacitu systému a výkonnost pozicování v prostředích s hustou koncentrací zařízení.

## Klíčové vlastnosti

- Identifikátor specifický pro uživatelské zařízení pro konfigurované plánování zdrojů SL-PRS
- Používá se ke skramblování CRC DCI formátu 3_0 pro aktivaci povolení na postranním spoji
- Podporuje operace konfigurovaného povolení typu 1 i typu 2
- Snižuje režii řídicí signalizace ve srovnání s dynamickými povoleními
- Umožňuje periodické a předvídatelné vysílání SL-PRS
- Zvyšuje spolehlivost a snižuje latenci v postranním spoji pro pozicovací procedury

## Související pojmy

- [SL-PRS – Sidelink Positioning Reference Signals](/mobilnisite/slovnik/sl-prs/)
- [CS-RNTI – Configured Scheduling Radio Network Temporary Identifier](/mobilnisite/slovnik/cs-rnti/)

## Definující specifikace

- **TS 38.321** (Rel-19) — NR MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [SL-PRS-CS-RNTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/sl-prs-cs-rnti/)
