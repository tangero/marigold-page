---
slug: "efap"
url: "/mobilnisite/slovnik/efap/"
type: "slovnik"
title: "EFAP – Edge Fading Amplitude Panning"
date: 2025-01-01
abbr: "EFAP"
fullName: "Edge Fading Amplitude Panning"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/efap/"
summary: "Edge Fading Amplitude Panning (EFAP) je mediální zpracovatelská funkce 3GPP pro immersivní audio služby, zavedená v Release 18. Dynamicky upravuje úrovně zvukového signálu mezi různými reproduktory ne"
---

EFAP je mediální funkce 3GPP Release 18, která dynamicky upravuje úrovně zvuku mezi reproduktory nebo objekty, aby vytvořila fadingový efekt pro zvýšený prostorový realismus v immersivních službách, jako je XR.

## Popis

Edge Fading Amplitude Panning (EFAP) je standardizovaná technika zpracování médií definovaná 3GPP pro immersivní audio služby, konkrétně v kontextu 5G Media Streaming ([5GMS](/mobilnisite/slovnik/5gms/)). Je to funkce, která manipuluje s audio objekty nebo kanály za účelem vytvoření plynulých amplitudových přechodů, neboli 'fadingů', mezi různými prostorovými pozicemi nebo reproduktory. Tato technika je klíčová pro vykreslování přesvědčivého prostorového audia, kde se zdroje zvuku musí zdánlivě plynule pohybovat kolem posluchače nebo kde by audio mělo plynule přecházet z jednoho výstupního kanálu do druhého (např. když posluchač otočí hlavou v prostředí [VR](/mobilnisite/slovnik/vr/)). EFAP pracuje se zvukovými signály, které jsou součástí popisu scény, často využívající formáty jako MPEG-I Immersive Audio.

Architektonicky je EFAP implementován jako součást v rámci mediálního zpracovatelského enginu, který může sídlit v síťovém uzlu pro zpracování médií (jako je edge server v prostředí 5G [MEC](/mobilnisite/slovnik/mec/)) nebo v zařízení uživatele (UE). Funkce jako vstup přijímá audio objekty s přidruženými metadaty definujícími jejich požadovanou prostorovou pozici. Jak se metadata o pozici v čase mění (např. v důsledku interakce uživatele nebo předpřipravené animace), EFAP vypočítává potřebné koeficienty zesílení pro každý výstupní kanál (např. levý, pravý, obklopující reproduktory nebo binaurální vykreslování pro sluchátka), aby vytvořil vjem pohybu. Aspekt 'Edge Fading' odkazuje na jeho schopnost zpracovávat přechody konkrétně na hranicích neboli 'okrajích' audio scény nebo mezi různými audio zónami, čímž zajišťuje, že nedojde k náhlým skokům nebo klikáním ve zvuku.

Jak EFAP funguje, zahrnuje kontinuální interpolaci amplitudových koeficientů na základě trajektorie pozice audio objektu. Například, pokud je audio objekt naprogramován k pohybu z předního levého reproduktoru na přední pravý reproduktor, EFAP bude po dobu trvání pohybu postupně snižovat zesílení aplikované na přední levý kanál a současně zvyšovat zesílení pro přední pravý kanál. Algoritmy zajišťují, že vnímaná hlasitost zůstává konzistentní (aby nedocházelo k nezamýšleným změnám hlasitosti) a že je dodržován panningový zákon (např. panning s konstantním výkonem) pro přirozené prostorové vnímání. Jeho role v síti spočívá v umožnění vysoce kvalitních immersivních mediálních zážitků s nízkou latencí jako součástí vylepšeného mobilního širokopásmového přenosu (eMBB) a služeb [XR](/mobilnisite/slovnik/xr/) v 5G, přičemž často využívá edge computing k odlehčení komplexního audio zpracování z UE.

## K čemu slouží

Edge Fading Amplitude Panning existuje za účelem řešení problému vytváření plynulých, realistických a artefaktů prostých prostorových audio přechodů v immersivních mediálních aplikacích. Jak se spotřeba médií vyvíjí směrem k videu 360°, virtuální realitě ([VR](/mobilnisite/slovnik/vr/)), rozšířené realitě ([AR](/mobilnisite/slovnik/ar/)) a cloudovému hraní, jednoduché stereo nebo kanálové audio je nedostatečné. Tyto aplikace vyžadují, aby se audio objekty dynamicky pohybovaly v 3D prostoru vzhledem k úhlu pohledu uživatele. Bez technik jako je EFAP mohou být audio přechody drsné, nespojité nebo mohou způsobovat nežádoucí percepční efekty, jako jsou posuny fantomového středu nebo poklesy hlasitosti, což narušuje pocit ponoření.

Motivace pro jeho standardizaci v 3GPP Release 18 je hnána snahou průmyslu o interoperabilní, vysoce kvalitní doručování immersivních médií přes 5G sítě. Před standardizací využívalo vykreslování immersivního audia proprietární nebo neinteroperabilní panningové techniky, což mohlo vést k nekonzistentním zážitkům na různých zařízeních a platformách. Definováním EFAP jako normativní funkce v rámci frameworku [5GMS](/mobilnisite/slovnik/5gms/) umožňuje 3GPP tvůrcům obsahu, poskytovatelům služeb a výrobcům zařízení mít společný referenční bod pro implementaci prostorového audio panningu. Tím se řeší omezení ad-hoc přístupů a usnadňuje se škálovatelné nasazení immersivních služeb, což zajišťuje, že VR zážitek streamovaný z cloudového serveru na 5G zařízení se sluchátky doručí zamýšlený pohyb audia s vysokou věrností.

## Klíčové vlastnosti

- Standardizovaný amplitudový panning pro plynulé prostorové audio přechody
- Podporuje dynamické audio objekty s časově proměnnými metadaty o pozici
- Navrženo pro integraci v rámci architektury 5G Media Streaming (5GMS)
- Umožňuje konzistentní vykreslování immersivního audia na různých zařízeních a platformách
- Zpracovává edge/crossfading mezi audio kanály nebo zónami, aby se předešlo artefaktům
- Lze nasadit na síťovém edge (MEC) pro odlehčení výpočetního výkonu

## Související pojmy

- [5GMS – 5G Media Streaming](/mobilnisite/slovnik/5gms/)

## Definující specifikace

- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description

---

📖 **Anglický originál a plná specifikace:** [EFAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/efap/)
