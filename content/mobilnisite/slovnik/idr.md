---
slug: "idr"
url: "/mobilnisite/slovnik/idr/"
type: "slovnik"
title: "IDR – Instantaneous Decoding Refresh"
date: 2025-01-01
abbr: "IDR"
fullName: "Instantaneous Decoding Refresh"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/idr/"
summary: "Funkce ve videokódování, zejména H.264/AVC a H.265/HEVC, která definuje typ videosnímku (IDR snímek). Resetuje stav dekodéru a zajišťuje, že všechny následující snímky lze dekódovat bez odkazu na jaký"
---

IDR je funkce videokódování, která definuje typ snímku resetující stav dekodéru, což umožňuje náhodný přístup a obnovu po chybě tím, že všechny následující snímky učiní nezávislými na předchozích datech.

## Popis

Instantaneous Decoding Refresh (IDR) je klíčový koncept v moderních standardech videokomprese, zejména H.264/[AVC](/mobilnisite/slovnik/avc/) (Advanced Video Coding) a H.265/[HEVC](/mobilnisite/slovnik/hevc/) (High Efficiency Video Coding), jak je přijal a profiloval 3GPP pro multimediální služby jako [MBMS](/mobilnisite/slovnik/mbms/) a streamování. IDR snímek je speciální typ intra-kódovaného (I) snímku, který slouží jako silný synchronizační a náhodný přístupový bod ve videosnímku. Z pohledu dekódování příchod IDR snímku resetuje vyrovnávací paměť referenčních snímků dekodéru. To znamená, že žádný snímek dekódovaný po IDR snímku nesmí použít jako referenci pro prediktivní kódování jakýkoli snímek dekódovaný *před* tímto IDR snímkem.

Technicky je toto vynuceno pomocí typu [NAL](/mobilnisite/slovnik/nal/) (Network Abstraction Layer) jednotky a syntaktických prvků v hlavičce řezu. Když dekodér narazí na IDR snímek, označí všechny existující referenční snímky ve své vyrovnávací paměti dekódovaných snímků ([DPB](/mobilnisite/slovnik/dpb/)) jako "nepoužité pro referenci", čímž je efektivně vymaže. Všechny následující P (Predikované) a B (Biprediktivní) snímky pak mohou odkazovat pouze na snímky, které následují po tomto IDR snímku v dekódovacím pořadí. Tím se vytvoří čistý předěl v predikčním řetězci. Samotný IDR snímek je kódován pouze s využitím prostorové redundance uvnitř snímku (intra-predikce), což jej činí nezávisle dekódovatelným, ale také relativně velkým ve srovnání s inter-kódovanými snímky.

V kontextu služeb 3GPP, jako je Packet-Switched Streaming Service (PSS), Multimedia Broadcast/Multicast Service (MBMS) nebo Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/) ([DASH](/mobilnisite/slovnik/dash/)), jsou IDR snímky strategicky vkládány do videoproudu. Jejich role je mnohostranná: umožňují náhodný přístup pro uživatele připojující se k vysílání nebo přecházející v rámci proudu, poskytují bod obnovy po ztrátě nebo poškození dat (protože dekódování může čistě restartovat od IDR) a usnadňují přepínání kanálů v mobilních TV službách tím, že poskytují časté vstupní body. Interval vkládání IDR snímků je klíčový kompromis mezi výkonem náhodného přístupu/odolnosti vůči chybám a kódovací účinností, protože častější IDR snímky zvyšují datový tok, ale zlepšují přístupnost.

## K čemu slouží

Účelem snímku Instantaneous Decoding Refresh (IDR) je poskytnout garantované, čisté body pro (re-)inicializaci dekodéru v rámci prediktivně kódované videosekvence. Videokomprese silně závisí na časové predikci, kde jsou snímky (P a B snímky) kódovány vzhledem k dříve dekódovaným referenčním snímkům. To vytváří dlouhé řetězce závislosti. Bez mechanismu jako je IDR by dekodér, který začne uprostřed proudu, zaznamená ztrátu paketu nebo narazí na poškozený snímek, nebyl schopen správně rekonstruovat následující snímky, protože by mohly záviset na chybějících nebo chybných referenčních datech.

IDR tento problém řeší periodickým vkládáním snímku, který přeruší všechny predikční závislosti na minulosti. Byl motivován požadavky interaktivních a vysílacích služeb přes náchylné k chybám a dynamické kanály, jako jsou mobilní sítě. Pro služby jako videotelefonie, streamování a mobilní TV potřebují uživatelé být schopni okamžitě přepínat kanály nebo přecházet ve videu. IDR snímek poskytuje technický základ pro toto tím, že zajišťuje, že od tohoto bodu dále je dekódování soběstačné. Řeší omezení čistého přístupu s I-snímky formální definicí resetu stavu dekodéru ve standardu, čímž zajišťuje interoperabilitu. Jeho vytvoření a standardizace v rámci videokodeků byly nezbytné pro umožnění spolehlivých, náhodně přístupných videoslužeb v ekosystémech 3GPP, vyvažující vysokou kompresní účinnost dlouhodobé predikce s praktickými potřebami doručování a přehrávání.

## Klíčové vlastnosti

- Typ I-snímku, který resetuje vyrovnávací paměť referenčních snímků dekodéru
- Zajišťuje, že žádný následující snímek neodkazuje na jakýkoli snímek před IDR
- Umožňuje náhodný přístup pro přepínání kanálů a přecházení ve videu
- Poskytuje synchronizační bod pro obnovu po chybě po ztrátě dat
- Definován specifickými typy NAL jednotek v H.264/AVC a H.265/HEVC
- Kritický pro streamovací služby (DASH, HLS) a vysílání (MBMS)

## Související pojmy

- [HEVC – High Efficiency Video Coding](/mobilnisite/slovnik/hevc/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)

## Definující specifikace

- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.223** (Rel-19) — IMS Telepresence Client Specification
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TS 26.247** (Rel-19) — 3GPP Progressive Download & DASH over HTTP
- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.522** (Rel-19) — RTP for XR in 5G Systems
- **TS 26.851** (Rel-11) — Enhancements to Multimedia (EMM) for PSS, MMS, MBMS
- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TR 26.946** (Rel-19) — MBMS User Services Overview
- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks

---

📖 **Anglický originál a plná specifikace:** [IDR na 3GPP Explorer](https://3gpp-explorer.com/glossary/idr/)
