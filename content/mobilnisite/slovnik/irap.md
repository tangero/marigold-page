---
slug: "irap"
url: "/mobilnisite/slovnik/irap/"
type: "slovnik"
title: "IRAP – Intra Random Access Picture"
date: 2025-01-01
abbr: "IRAP"
fullName: "Intra Random Access Picture"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/irap/"
summary: "Intra Random Access Picture (IRAP) je koncept video kódování v rámci 3GPP standardu Dynamic Adaptive Streaming over HTTP (DASH) a souvisejících standardů pro doručování médií. Jedná se o kódovaný sním"
---

IRAP je kódovaný snímek ve standardech pro video streamování, který umožňuje náhodný přístup do video proudu pro operace jako přeskočení na jinou pozici, přepínání datového toku a obnovu po chybě.

## Popis

Intra Random Access Picture je specifický typ snímku ve video datovém proudu kódovaný pomocí kodeků jako H.264/[AVC](/mobilnisite/slovnik/avc/) nebo H.265/[HEVC](/mobilnisite/slovnik/hevc/). Technicky se jedná o kódovaný snímek, kde všechny řezy jsou intra-kódované řezy (I-řezy), což znamená, že jsou komprimovány pouze s využitím prostorové redundance v rámci stejného snímku, bez odkazu na jiné snímky. Díky tomu je IRAP samostatný a lze jej dekódovat nezávisle. V kontextu adaptivního streamování tvoří IRAP snímek spolu se všemi následujícími snímky v dekódovacím pořadí až do dalšího IRAP snímku segment „Random Access Point“. Tento segment lze dekódovat bez jakéhokoli odkazu na snímky, které mu v dekódovacím pořadí předcházejí, čímž efektivně vytváří dekódovatelný vstupní bod do kontinuálního proudu.

Architektura pro využití IRAP je definována v rámci specifikací 3GPP Packet-switched Streaming Service ([PSS](/mobilnisite/slovnik/pss/)) a Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/) ([DASH](/mobilnisite/slovnik/dash/)). Mezi klíčové komponenty patří mediální enkodér, který periodicky vkládá IRAP snímky podle definovaného intervalu nebo při změně scény; segmentátor, který zabalí mediální data do segmentů zarovnaných na hranice IRAP pro DASH; a soubor Media Presentation Description ([MPD](/mobilnisite/slovnik/mpd/)), který signalizuje dostupnost a časování těchto bodů náhodného přístupu klientovi. Klientovský přehrávač tyto informace využívá k provádění adaptace datového toku čistým přepnutím na segment z jiné reprezentace (proudu s jiným datovým tokem nebo rozlišením) začínající na IRAP snímku, čímž zajišťuje plynulé přehrávání bez dekódovacích chyb.

Jak to funguje v praxi, zahrnuje pečlivé zarovnání mezi kódováním, zabalováním a signalizací. Při video kódování je enkodér nakonfigurován tak, aby generoval IRAP snímky v pravidelných intervalech (např. každé 2 sekundy). Tyto snímky jsou výrazně větší než predikované (P nebo B) snímky, ale poskytují klíčové přístupové body. Pro doručování DASH je mediální soubor fragmentován do segmentů tak, že každý segment začíná IRAP snímkem. MPD udává počáteční čas každého segmentu vzhledem k časové ose prezentace. Když uživatel přejde na nový čas nebo se klient rozhodne přepnout na vyšší nebo nižší datový tok, vyžádá si segment z nové reprezentace, který obsahuje IRAP snímek nejbližší požadovanému času přehrávání. To zajišťuje, že se dekodér může z tohoto bodu správně inicializovat a začít dekódovat, čímž je zachováno kontinuální přehrávání.

## K čemu slouží

Koncept IRAP existuje pro řešení kritických problémů ve video streamování, zejména v adaptivním streamování přes [HTTP](/mobilnisite/slovnik/http/) ([DASH](/mobilnisite/slovnik/dash/)). Primárními problémy je umožnění náhodného přístupu (přeskočení na jinou pozici) v rámci proudu a usnadnění plynulého přepínání mezi různými zakódovanými verzemi stejného obsahu (adaptivní přepínání datového toku). Bez samostatných přístupových bodů by musel video přehrávač při přeskočení na novou pozici dekódovat všechny snímky od začátku proudu nebo od posledního plného klíčového snímku, což je neefektivní a pomalé. Podobně by přepínání datového toku uprostřed proudu způsobilo selhání dekódování, pokud by nový segment proudu závisel na snímcích ze starého proudu.

Historicky poskytovaly náhodný přístup jednoduché I-snímky (intra-kódované snímky), ale koncept IRAP v kontextu H.264/AVC a HEVC poskytuje formalizovanější a robustnější definici, která zahrnuje zpracování úvodních snímků (jako Broken Link Access pictures). Jeho přijetí ve standardech 3GPP (počínaje Rel-12) bylo motivováno přechodem průmyslu k adaptivnímu streamování založenému na HTTP jako dominantní metodě pro doručování videa přes mobilní a pevné sítě. 3GPP potřebovalo standardizovat, jak balit a signalizovat média pro spolehlivé, interoperabilní streamovací služby na zařízeních.

IRAP řeší omezení nezarovnaného přepínání proudů a neefektivního přeskočování. Tím, že vyžaduje, aby segmenty pro adaptivní streamování začínaly IRAP snímkem, zaručuje, že se klient může vždy čistě přepnout na jinou reprezentaci. To je zásadní pro poskytování vysoké kvality uživatelského zážitku (QoE), protože umožňuje plynulou adaptaci na měnící se šířku pásma sítě bez zavádění vizuálních artefaktů nebo přerušení přehrávání. Také umožňuje efektivní režimy speciálního přehrávání (rychlé přehrávání vpřed, zpět) a odolnost vůči chybám, protože přenosové chyby lze obnovit na další hranici IRAP.

## Klíčové vlastnosti

- Samostatný kódovaný snímek (všechny intra-kódované řezy) umožňující nezávislé dekódování
- Slouží jako bod náhodného přístupu pro přeskočení na jinou pozici a spojování proudů
- Povinný zarovnávací bod pro mediální segmenty DASH umožňující přepínání datového toku
- Definován v rámci standardů pro video kódování jako H.264/AVC a H.265/HEVC
- Signalizován v souboru Media Presentation Description (MPD) pro DASH klienty
- Umožňuje obnovu po chybě a funkce speciálního přehrávání ve streamování

## Související pojmy

- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)
- [HEVC – High Efficiency Video Coding](/mobilnisite/slovnik/hevc/)

## Definující specifikace

- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.223** (Rel-19) — IMS Telepresence Client Specification
- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.522** (Rel-19) — RTP for XR in 5G Systems
- **TS 26.822** (Rel-19) — 5G RTP Configurations Study Phase 2
- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services
- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services

---

📖 **Anglický originál a plná specifikace:** [IRAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/irap/)
