---
slug: "pser"
url: "/mobilnisite/slovnik/pser/"
type: "slovnik"
title: "PSER – Packet Set Error Rate"
date: 2026-01-01
abbr: "PSER"
fullName: "Packet Set Error Rate"
category: "QoS"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pser/"
summary: "Packet Set Error Rate (PSER) je metrika kvality služby (QoS) zavedená ve specifikaci 3GPP Release 18 pro pokročilé služby jako XR a průmyslový IoT. Měří podíl sad paketů, které nejsou úspěšně doručeny"
---

PSER je metrika kvality služby (QoS) 3GPP, která měří podíl sad paketů, které nebyly úspěšně doručeny v rámci požadovaného časového omezení (latence). Používá se pro služby s přísnými požadavky na spolehlivost a latenci, jako je XR.

## Popis

Packet Set Error Rate (PSER) je statistická metrika kvality služby (QoS) definovaná v rámci rámce QoS pro 5G. Kvantifikuje spolehlivost doručování paketů pro aplikace, kde jsou data organizována do logických skupin neboli 'sad paketů'. Sada paketů je kolekce paketů, které jsou sémanticky propojeny a mají společný termín doručení. PSER se vypočítá jako poměr sad paketů, u kterých dojde k alespoň jednomu selhání doručení paketu (např. ztráta, nadměrné zpoždění přesahující časový limit nebo doručení mimo požadované pořadí), k celkovému počtu přenesených sad paketů.

Metrika funguje ve spojení s dalšími parametry QoS, jako je rozpočet zpoždění paketu ([PDB](/mobilnisite/slovnik/pdb/)) a chybovost paketů ([PER](/mobilnisite/slovnik/per/)). PSER však poskytuje ucelenější pohled pro aplikace, kde je integrita celé datové jednotky (sady) prvořadá. Síť využívá cíl PSER spolu s přidruženým časovým omezením (často maximální povolené zpoždění paketu) k rozhodování o přidělování prostředků a plánování. Například u streamu rozšířené reality může být snímek složen z více paketů; PSER zajišťuje, že celý snímek je doručen správně a včas, protože ztráta i jednoho paketu může zhoršit uživatelský zážitek.

Z architektonického hlediska je PSER součástí tabulky 5G QoS indikátoru ([5QI](/mobilnisite/slovnik/5qi/)) a přidružených popisů toků QoS. Je signalizován mezi uživatelským zařízením (UE), rádiovou přístupovou sítí (RAN) a jádrem sítě (konkrétně funkcí správy relace – [SMF](/mobilnisite/slovnik/smf/)) k nastavení požadovaných charakteristik služby. Plánovač RAN je klíčovou součástí zodpovědnou za dosažení cíle PSER a využívá techniky jako prioritní plánování, redundance (např. prostřednictvím duplikace paketů) nebo strategie hybridního automatického opakování ([HARQ](/mobilnisite/slovnik/harq/)) přizpůsobené pro spolehlivost na úrovni sad.

Role PSER je zásadní pro umožnění deterministické komunikace v 5G-Advanced a novějších verzích. Posouvá se od záruk na úrovni jednotlivých paketů k zárukám na úrovni datových jednotek, což je zásadní pro časově citlivé aplikace. Jeho specifikace napříč dokumenty, jako je TS 23.501 (systémová architektura), TS 38.300 (celkový popis RAN) a TS 38.835 (práce na NR pro průmyslový IoT), zdůrazňuje jeho integraci jak do definice základní služby, tak do procedur rádiového rozhraní.

## K čemu slouží

PSER byl vytvořen, aby řešil přísné a komplexní požadavky na spolehlivost vznikajících aplikací éry 5G-Advanced a 6G, zejména rozšířené reality ([XR](/mobilnisite/slovnik/xr/)), cloudového hraní a ultra-spolehlivé komunikace s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) pro průmyslovou automatizaci. Tradiční metriky QoS, jako je chybovost paketů ([PER](/mobilnisite/slovnik/per/)) a rozpočet zpoždění paketu (PDB), poskytují záruky pro jednotlivé pakety, ale nedostatečně zachycují výkonnostní potřeby aplikací, kde jsou data strukturována do skupin (např. video snímek, řídicí příkaz s více parametry nebo synchronizovaná dávka senzorů). Ztráta jediného paketu v takové skupině může způsobit, že celá datová jednotka je nepoužitelná, i když je průměrná PER nízká.

Motivace vychází z omezení předchozích přístupů. Zajištění nízké PER pro každý paket je často neefektivní a náročné na zdroje. PSER umožňuje síti optimalizovat využití prostředků zaměřením na úspěšné doručení logicky kompletních sad v časovém okně, čímž poskytuje metriku spolehlivosti více zaměřenou na aplikaci. To umožňuje síťovému řezání a rámcům QoS podporovat služby s 'omezenou spolehlivostí' – koncept, kde mohou být občasná selhání sad tolerovatelná, pokud jsou omezena v rámci statistického limitu, což umožňuje flexibilnější a efektivnější provoz sítě ve srovnání s tradičními modely spolehlivosti 'pěti devítek' (99,999 %) na úrovni paketu, které jsou často nadměrně dimenzovány.

Historicky, jak se 3GPP vyvíjelo od vylepšeného mobilního širokopásmového přístupu (eMBB) k masivnímu IoT a kritickému IoT, stala se zřejmou potřeba podrobnějších a různorodějších metrik QoS. PSER, zavedený ve verzi Release 18 jako součást prací na vylepšeném XR a průmyslovém IoT, představuje významný krok ve zdokonalování nástrojů QoS. Umožňuje poskytovatelům služeb definovat a garantovat smlouvy o úrovni služeb (SLA), které přímo odpovídají percepční nebo operační kvalitě koncové uživatelské aplikace, což usnadňuje nové zdroje příjmů a umožňuje skutečně deterministický bezdrátový výkon pro průmysl 4.0.

## Klíčové vlastnosti

- Metrika spolehlivosti na úrovni sad měřící míru selhání logických skupin paketů
- Definována ve spojení s maximálním časovým omezením pro sadu paketů
- Integrována do rámce QoS pro 5G a tabulky 5QI
- Umožňuje plánování prostředků v RAN s ohledem na aplikaci
- Podporuje statistickou omezenou spolehlivost pro efektivitu
- Klíčová pro deterministický výkon v aplikacích XR a průmyslového IoT

## Související pojmy

- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)
- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TR 38.835** (Rel-18) — Technical Report on XR Enhancements for NR

---

📖 **Anglický originál a plná specifikace:** [PSER na 3GPP Explorer](https://3gpp-explorer.com/glossary/pser/)
