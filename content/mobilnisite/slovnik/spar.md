---
slug: "spar"
url: "/mobilnisite/slovnik/spar/"
type: "slovnik"
title: "SPAR – Spatial Reconstruction"
date: 2025-01-01
abbr: "SPAR"
fullName: "Spatial Reconstruction"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/spar/"
summary: "Technika zavedená ve specifikaci 3GPP Release 18 pro rekonstrukci prostorových informací, jako je stav kanálu nebo data pro beamforming, z komprimované nebo omezené zpětné vazby. Zvyšuje efektivitu a"
---

SPAR je technika z Release 18 pro rekonstrukci prostorových informací, jako je stav kanálu, z komprimované zpětné vazby, která zvyšuje efektivitu sítě tím, že umožňuje přesné prostorové zpracování s nižší režií.

## Popis

Spatial Reconstruction (SPAR) je rámec definovaný ve specifikacích 3GPP, především v TS 26.253, zaměřený na efektivní získávání a využití prostorových informací v bezdrátových sítích. Funguje tak, že rekonstruuje vysoce dimenzionální prostorová data, jako je informace o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)) nebo beamformingové vektory, z nižší-dimenzionálních, komprimovaných reportů zpětné vazby odesílaných uživatelským zařízením (UE). Proces zahrnuje pokročilé algoritmy zpracování signálu, včetně kompresivního snímání a inferencí založených na strojovém učení, k interpolaci nebo predikci úplných prostorových charakteristik rádiového kanálu. Tyto rekonstruované informace jsou pak sítí, konkrétně gNB v 5G NR, použity k optimalizaci víceanténních přenosů, včetně Massive [MIMO](/mobilnisite/slovnik/mimo/) a beamformingových operací, čímž se zlepšuje spektrální účinnost a spolehlivost spojení.

Architektonicky je SPAR implementován ve vrstvě RAN a zahrnuje komponenty jak v UE, tak v gNB. UE měří downlinkový kanál a aplikuje kompresní techniky ke snížení objemu zpětné vazby, která je přenášena přes uplinkové řídicí kanály. gNB po přijetí této komprimované zpětné vazby využívá rekonstrukční engine – klíčovou funkční komponentu – k obnovení prostorové matice kanálu. Tento engine může využívat kodebooky, neuronové sítě nebo jiné parametrické modely standardizované nebo konfigurované sítí. Přesnost rekonstrukce je klíčová a závisí na faktorech, jako je kompresní poměr, periodicita zpětné vazby a mobilita UE.

Role SPAR je nedílnou součástí pokročilých anténních systémů, zejména v pásmech mmWave kmitočtového rozsahu 2 (FR2), kde je správa beamů prvořadá. Minimalizací režie zpětné vazby šetří uplinkové zdroje a snižuje latenci, což umožňuje častější a přesnější prostorové adaptace. To podporuje případy užití vyžadující vysokou propustnost a nízkou latenci, jako je rozšířené mobilní širokopásmové připojení (eMBB) a ultra-spolehlivá komunikace s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)). Tato technika je v souladu s probíhajícími snahami 3GPP o zvyšování kapacity sítě a uživatelského zážitku prostřednictvím inteligentních optimalizací RAN.

## K čemu slouží

SPAR byl vytvořen, aby řešil rostoucí režii spojenou se zpětnou vazbou [CSI](/mobilnisite/slovnik/csi/) v moderních [MIMO](/mobilnisite/slovnik/mimo/) systémech, zejména s rostoucím počtem antén při nasazeních Massive MIMO. V systémech před Release 18 vyžadovalo podrobné reportování CSI značné uplinkové zdroje, což vedlo k neefektivitám a potenciálním úzkým hrdlům. SPAR to řeší tím, že umožňuje obnovení prostorových informací s vysokou věrností z komprimované zpětné vazby, čímž vyvažuje přesnost a spotřebu zdrojů.

Historicky se používaly mechanismy omezené zpětné vazby, jako je precoding založený na kodebooku, které však často zápasily se škálovatelností a adaptabilitou v dynamických podmínkách kanálu. SPAR zavádí sofistikovanější rekonstrukční metody, motivované potřebou podporovat aplikace náročné na šířku pásma a hustá nasazení sítí v 5G-Advanced. Řeší omezení předchozích přístupů využitím pokroků ve zpracování signálu a strojovém učení a poskytuje flexibilní rámec, který se dokáže přizpůsobit různým síťovým podmínkám a možnostem UE.

## Klíčové vlastnosti

- Mechanismy komprimované zpětné vazby pro prostorová data
- Rekonstrukční algoritmy pro obnovení stavu kanálu
- Podpora pro optimalizaci Massive MIMO a beamformingu
- Snížení režie uplinkového řízení
- Zvýšená spektrální účinnost díky přesnému prostorovému zpracování
- Konfigurovatelné rekonstrukční modely na základě síťových podmínek

## Související pojmy

- [CSI – Combined CS and IMS Services](/mobilnisite/slovnik/csi/)

## Definující specifikace

- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description

---

📖 **Anglický originál a plná specifikace:** [SPAR na 3GPP Explorer](https://3gpp-explorer.com/glossary/spar/)
