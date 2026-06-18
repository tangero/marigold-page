---
slug: "pei-o"
url: "/mobilnisite/slovnik/pei-o/"
type: "slovnik"
title: "PEI-O – Paging Early Indication-Occasion"
date: 2025-01-01
abbr: "PEI-O"
fullName: "Paging Early Indication-Occasion"
category: "Radio Access Network"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/pei-o/"
summary: "Specifický časový okamžik uvnitř cyklu stránkování, ve kterém může být vyslán signál Paging Early Indication (PEI). Informuje UE ve stavu RRC_IDLE nebo RRC_INACTIVE, zda mají monitorovat následující p"
---

PEI-O je specifický časový okamžik uvnitř cyklu stránkování, ve kterém může být vyslán signál Paging Early Indication, aby informoval UE v idle nebo inactive stavu, zda mají monitorovat následující paging occasion za účelem úspory energie.

## Popis

Paging Early Indication-Occasion (PEI-O) je koncept přístupové sítě (RAN) zavedený v 5G NR pro zvýšení energetické účinnosti UE. Označuje předdefinovaný časový zdroj (okamžik), ve kterém může gNB vyslat signál Paging Early Indication ([PEI](/mobilnisite/slovnik/pei/)). Tento signál je krátký indikátor fyzické vrstvy s nízkou složitostí, vysílaný před vlastním Paging Occasion ([PO](/mobilnisite/slovnik/po/)). UE pracující v úsporných režimech, konkrétně ve stavech [RRC](/mobilnisite/slovnik/rrc/)_IDLE nebo RRC_INACTIVE, se probudí ve svém nakonfigurovaném PEI-O, aby tento signál detekovaly. Samotný PEI signál je jednoduchý binární indikátor, často přenášený pomocí formátu Downlink Control Information ([DCI](/mobilnisite/slovnik/dci/)) zakódovaného [PEI-RNTI](/mobilnisite/slovnik/pei-rnti/), který informuje skupinu UE, zda jsou pro ně v nadcházejícím PO přítomny paging zprávy.

Operační postup začíná tím, že síť nakonfiguruje UE paging parametry, včetně jejich Paging Frame ([PF](/mobilnisite/slovnik/pf/)), Paging Occasion (PO) a nyní také odpovídajícího PEI-O. Tato konfigurace je doručena systémovou informací nebo dedikovanou RRC signalizací. PEI-O je časově umístěn před přidruženým PO, což umožňuje UE nejprve zkontrolovat PEI. Pokud PEI indikuje 'negativní' stav (žádné stránkování pro monitorovanou skupinu), může se UE okamžitě vrátit do stavu hlubokého spánku, aniž by musela aktivovat celý řetězec přijímače pro dekódování [PDCCH](/mobilnisite/slovnik/pdcch/) a [PDSCH](/mobilnisite/slovnik/pdsch/) během PO. Toto přeskočení ušetří značné množství energie baterie. Pokud PEI indikuje 'pozitivní' stav, UE zůstane probuzena, aby monitorovala svůj PO kvůli možné paging zprávě.

Z architektonického hlediska je PEI-O zdroj definovaný v rámci struktury NR rámu. Jeho periodicita a časování jsou odvozeny od identity UE a paging konfigurace, což zajišťuje sladění mezi UE a gNB. RRC a MAC vrstvy gNB určí, která UE je třeba stránkovat, a poté instruují fyzickou vrstvu, aby vyslala příslušný PEI signál ve vypočtených PEI-O. Tento mechanismus je klíčovou součástí vylepšeného přerušovaného příjmu (eDRX) a funkcí úspory energie v 5G. Optimalizuje kompromis mezi latencí stránkování a životností baterie UE, což je obzvláště kritické pro hromadná IoT nasazení a neustále zapnutá spotřebitelská zařízení, protože drasticky snižuje energii spotřebovanou během častých cyklů monitorování stránkování.

## K čemu slouží

PEI-O byl vytvořen, aby řešil kritickou výzvu spotřeby energie UE, zejména pro zařízení, která tráví většinu času v stavech s nízkou spotřebou (RRC_IDLE/INACTIVE), ale musí se periodicky probouzet a kontrolovat paging zprávy. Tradiční přístup vyžadoval, aby UE plně dekódovala PDCCH při každém Paging Occasion, což je operace s vysokou energetickou náročností, i když pro ně není určena žádná paging zpráva. To vedlo k neefektivnímu vybíjení baterie, což byla hlavní omezení pro IoT zařízení s cílem životnosti baterie na desetiletí i pro výdrž baterie smartphonů.

Zavedení PEI-O ve 3GPP Release 17 je součástí širší pracovní položky 'NR Power Saving'. Řeší to přidáním kontrolního bodu probouzení s nízkou spotřebou. Motivace vychází z potřeby škálovat IoT a zlepšit uživatelský zážitek. Tím, že umožní UE provést detekci s velmi nízkou složitostí (PEI signál) předtím, než se zaváže k plnému dekódování paging kanálu, jsou energetické náklady na 'falešná probuzení' téměř eliminovány. Tato inovace přímo prodlužuje životnost baterie pro širokou škálu zařízení, aniž by ovlivnila schopnost sítě je dosáhnout s nízkou latencí, když je to nutné. Představuje evoluci od paging mechanismu LTE, zavádějící další, efektivní krok filtrování řízený sítí.

## Klíčové vlastnosti

- Předdefinovaný časový zdroj pro vysílání signálu Paging Early Indication
- Konfigurováno pro UE nebo skupinu UE prostřednictvím RRC nebo systémové informace
- Časově umístěn před přidruženým Paging Occasion (PO)
- Umožňuje UE provést detekci signálu s nízkou složitostí před plným dekódováním stránkování
- Integrální součást vylepšených funkcí úspory energie 5G NR
- Snižuje spotřebu energie pro UE ve stavech RRC_IDLE a RRC_INACTIVE

## Související pojmy

- [PEI-RNTI – Paging Early Indication Radio Network Temporary Identifier](/mobilnisite/slovnik/pei-rnti/)

## Definující specifikace

- **TS 38.304** (Rel-19) — UE RRC_IDLE and RRC_INACTIVE Procedures
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive

---

📖 **Anglický originál a plná specifikace:** [PEI-O na 3GPP Explorer](https://3gpp-explorer.com/glossary/pei-o/)
