---
slug: "or"
url: "/mobilnisite/slovnik/or/"
type: "slovnik"
title: "OR – Optimal Routeing"
date: 2025-01-01
abbr: "OR"
fullName: "Optimal Routeing"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/or/"
summary: "Mechanismus směrování hovorů v sítích GSM/UMTS, který určuje nejefektivnější cestu pro hovor iniciovaný mobilním zařízením k dosažení cíle, s přihlédnutím k faktorům jako je poloha účastníka a topolog"
---

OR je mechanismus směrování hovorů v sítích GSM/UMTS, který určuje nejefektivnější cestu pro hovor iniciovaný mobilním zařízením s ohledem na polohu účastníka a topologii sítě za účelem optimalizace zdrojů a zkrácení doby navazování.

## Popis

Optimal Routeing (OR, optimální směrování) je servisní funkce definovaná ve specifikacích 3GPP pro jádrové sítě GSM a UMTS. Jejím hlavním účelem je zvýšit efektivitu procedur navazování hovorů, zejména pro hovory iniciované mobilním zařízením. Když mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) zahájí hovor, síť musí určit, jak směrovat signalizaci hovoru a následný provoz ke správnému cíli, kterým může být jiný mobilní uživatel, účastník pevné sítě nebo servisní uzel. Tradiční směrování může používat výchozí nebo statickou cestu. OR zavádí do tohoto procesu inteligenci tím, že umožňuje síti vybrat optimální cestu na základě dynamických kritérií.

Architektura pro OR zahrnuje několik entit jádrové sítě, především Mobile Switching Centre ([MSC](/mobilnisite/slovnik/msc/)). MSC obsluhující volajícího účastníka přijme požadavek na navázání hovoru. Pomocí OR logiky, která může vycházet z dat účastníka, aktuálních informací o poloze a konfigurace sítě, MSC vyhodnocuje možné směrovací cesty. Cílem je minimalizovat počet síťových uzlů (jako jsou další MSC nebo tranzitní přepínače) zapojených do spojení, snížit signalizační zatížení a potenciálně snížit přenosové náklady. Rozhodnutí může zahrnovat směrování hovoru přímo k cílovému MSC, je-li to možné, nebo přes nejefektivnější bránu.

Fungování OR je integrováno do procedur řízení hovoru. Během nastavování Initial Address Message ([IAM](/mobilnisite/slovnik/iam/)) v signalizaci [SS7](/mobilnisite/slovnik/ss7/) použije zdrojové MSC OR algoritmy. Tyto algoritmy mohou zohledňovat číslo volané strany, domovskou [PLMN](/mobilnisite/slovnik/plmn/) ([HPLMN](/mobilnisite/slovnik/hplmn/)) volajícího účastníka nebo jeho aktuální navštívenou PLMN ([VPLMN](/mobilnisite/slovnik/vplmn/)) a jakékoli specifické směrovací politiky definované operátorem sítě. Výběr není vždy geograficky nejkratší cestou, ale z pohledu síťových zdrojů nejefektivnější, vyhýbající se zbytečným mezisíťovým propojením nebo mezinárodním přepínačům, pokud existuje přímá cesta. Jeho úlohou je zefektivnit provoz jádrové sítě, čímž zlepšuje celkovou kvalitu služeb a provozní ekonomiku.

## K čemu slouží

Optimal Routeing byl zaveden, aby řešil neefektivity při navazování hovorů v rané mobilní telefonii. V počátečních sítích GSM mohlo být směrování hovorů suboptimální, často následovalo předem dané cesty přes více přepínacích center, i když bylo dostupné přímější spojení. To vedlo ke zvýšenému signalizačnímu provozu, delší době navazování hovorů a vyššímu vytížení přenosových zdrojů, což mohlo následně ovlivnit kapacitu sítě a provozní náklady. Primární motivací bylo optimalizovat využití síťových zdrojů a zlepšit uživatelský zážitek snížením prodlevy po vytočení čísla.

Historický kontext vychází z expanze sítí GSM a složitosti zavedené roamingem. Když účastník přechází do jiné sítě nebo země, cesta směrování hovoru z navštíveného [MSC](/mobilnisite/slovnik/msc/) zpět do domovské sítě a poté k cíli se mohla stát spletitou. OR to řeší tím, že umožňuje navštívenému MSC analyzovat cíl a potenciálně směrovat hovor přímoji, například přes mezinárodní bránu bližší cíli, namísto vždy prvního směrování zpět do HPLMN. Řešil tak omezení statických směrovacích tabulek a jednoduchých přístupů směrování přes domovskou síť, a poskytl dynamické, nákladově efektivní a na výkon orientované řešení.

## Klíčové vlastnosti

- Dynamický výběr cesty na základě aktuálních dat o účastníkovi a síti v reálném čase
- Snížení signalizačního zatížení a počtu uzlů zapojených do hovoru
- Integrace s existujícími procedurami řízení hovoru MSC a signalizace SS7
- Zohlednění čísel volajícího a volané strany pro optimalizaci cesty
- Podpora pro národní i mezinárodní scénáře hovorů
- Konfigurovatelné směrovací politiky definované operátory sítě

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.826** (Rel-17) — Study on 5G for Critical Medical Applications
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 26.094** (Rel-19) — AMR Voice Activity Detector (VAD) Specification
- **TS 26.194** (Rel-19) — Voice Activity Detector for AMR-WB DTX
- **TS 46.042** (Rel-19) — GSM Half-Rate Voice Activity Detector Specification
- **TS 46.082** (Rel-19) — GSM Enhanced Full Rate Voice Activity Detector

---

📖 **Anglický originál a plná specifikace:** [OR na 3GPP Explorer](https://3gpp-explorer.com/glossary/or/)
