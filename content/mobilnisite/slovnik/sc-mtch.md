---
slug: "sc-mtch"
url: "/mobilnisite/slovnik/sc-mtch/"
type: "slovnik"
title: "SC-MTCH – Single Cell Multicast Transport Channel"
date: 2025-01-01
abbr: "SC-MTCH"
fullName: "Single Cell Multicast Transport Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sc-mtch/"
summary: "Transportní kanál používaný ve funkci SC-PTM v LTE pro doručování vícebodových dat více uživatelským zařízením (UE) v rámci jedné buňky. Umožňuje efektivní vysílací/vícebodové služby, jako jsou varová"
---

SC-MTCH je jednobuněčný vícebodový transportní kanál (Single Cell Multicast Transport Channel) používaný ve funkci SC-PTM v LTE pro efektivní doručování vícebodových dat více uživatelům v rámci jedné buňky, čímž optimalizuje využití rádiových prostředků.

## Popis

Jednobuněčný vícebodový transportní kanál (SC-MTCH) je downlink transportní kanál definovaný v architektuře LTE rádiového přístupového sítě (RAN), konkrétně pro režim přenosu Single-Cell Point-to-Multipoint ([SC-PTM](/mobilnisite/slovnik/sc-ptm/)). Funguje pod kontrolou eNodeB a je mapován na fyzický downlink sdílený kanál ([PDSCH](/mobilnisite/slovnik/pdsch/)) pro přenos na fyzické vrstvě. SC-MTCH je logický kanál, který přenáší vlastní vícebodová nebo vysílací uživatelská data, jako je multimediální obsah, nouzová varování nebo aktualizace softwaru, určená pro skupinu uživatelských zařízení (UE), která se připojila ke konkrétní vícebodové skupině. Jde o jednosměrný kanál ze sítě k UE a nepodporuje uplink zpětnou vazbu ani retransmise na vrstvě [MAC](/mobilnisite/slovnik/mac/), což odpovídá jeho vysílací povaze.

Z pohledu protokolového zásobníku existuje SC-MTCH na vrstvě řízení přístupu k médiu (MAC). eNodeB plánuje přenosy SC-MTCH pomocí specifického identifikátoru logického kanálu a skupinového dočasného identifikátoru rádiové sítě ([RNTI](/mobilnisite/slovnik/rnti/)), konkrétně Single Cell Notification RNTI ([SC-N-RNTI](/mobilnisite/slovnik/sc-n-rnti/)) nebo Group RNTI ([G-RNTI](/mobilnisite/slovnik/g-rnti/)), aby označil, která UE mají přenos dekódovat. Data na SC-MTCH jsou přenášena v protokolových datových jednotkách ([PDU](/mobilnisite/slovnik/pdu/)) vrstvy MAC. Na rozdíl od jednobodových kanálů SC-MTCH nepoužívá pro spolehlivost hybridní automatické opakování požadavku ([HARQ](/mobilnisite/slovnik/harq/)); místo toho se může v případě potřeby služby spoléhat na korekci chyb dopředným kódováním (FEC) na aplikační vrstvě nebo na schémata retransmise na vyšších vrstvách. Kanál je eNodeB dynamicky konfigurován a uvolňován na základě přítomnosti aktivních vícebodových relací a přihlášených UE v buňce.

Provoz SC-MTCH je úzce integrován s řídicím mechanismem SC-PTM. Před zahájením přenosu dat na SC-MTCH eNodeB použije jednobuněčný vícebodový řídicí kanál (SC-MCCH) k oznámení konfigurace a plánovacích informací pro dostupné SC-MTCH. UE zájemci o konkrétní vícebodovou službu monitorují SC-MCCH, aby získaly potřebné parametry, jako je přidružený G-RNTI a časově-frekvenční prostředky (subrámy), kde bude SC-MTCH přenášen. Po konfiguraci UE použije G-RNTI k 'dešifrování' PDCCH, který ukazuje na prostředky PDSCH nesoucí data SC-MTCH. Tato architektura umožňuje koexistenci více SC-MTCH (pro různé služby) v jedné buňce, z nichž každý je identifikován jedinečným dočasným mobilním skupinovým identifikátorem (TMGI) na vrstvě NAS a spravován pomocí odlišných konfigurací logických kanálů na vrstvě RRC.

## K čemu slouží

SC-MTCH byl zaveden, aby poskytl standardizovaný, efektivní mechanismus pro poskytování vícebodových a vysílacích služeb v rámci jedné LTE buňky, a reagoval tak na rostoucí poptávku po skupinových komunikačních službách. Před SC-PTM a SC-MTCH se LTE primárně spoléhalo na službu Multimedia Broadcast Multicast Service (MBMS) prostřednictvím MBSFN (Multicast-Broadcast Single Frequency Network), která vyžadovala komplexní synchronizaci napříč více buňkami a byla vhodnější pro širokoplošná vysílání videa ve vysoké kvalitě. Pro mnoho aplikací, jako jsou lokalizované komunikace pro veřejnou bezpečnost, cílená reklama nebo aktualizace softwaru zařízení v konkrétní oblasti, je jednobuněčné řešení praktičtější a efektivnější z hlediska prostředků.

Vytvoření SC-MTCH vyřešilo problém neefektivního jednobodového replikování pro skupinové služby. Bez vícebodového kanálu by síť musela pro každé UE přijímající stejný obsah zřizovat individuální vyhrazené přenosy (prostřednictvím DTCH), čímž by duplikovala datový proud pro každého uživatele a spotřebovávala nadměrné downlink rádiové prostředky a výpočetní výkon eNodeB. SC-MTCH umožňuje jediný přenos datového paketu přes rozhraní vzduchu, který mohou současně přijímat všechna přihlášená UE, což dramaticky zlepšuje spektrální účinnost a snižuje zatížení sítě pro skupinově orientovaný provoz. To je obzvláště kritické pro scénáře komunikace typu stroj-stroj (MTC) nebo nasazení internetu věcí (IoT), kde velký počet zařízení může potřebovat přijmout stejnou konfiguraci nebo aktualizaci firmwaru.

Historicky byl SC-MTCH součástí vylepšení LTE pro komunikaci typu stroj-stroj (eMTC) a kritické komunikace zavedených ve 3GPP Release 13. Zaplnil mezeru v ekosystému LTE tím, že poskytl odlehčenou, buňkově specifickou vícebodovou schopnost, která doplňuje širokoplošné MBMS založené na MBSFN. Jeho návrh upřednostňuje jednoduchost a nízkou režii, což jej činí vhodným pro služby, které nevyžadují přísnou synchronizaci a kombinační zisky MBSFN, ale stále těží z úspory prostředků při vícebodovém doručování.

## Klíčové vlastnosti

- Přenáší uživatelská rovinnová data pro vícebodové/vysílací služby v rámci jedné LTE buňky.
- Je mapován na fyzický downlink sdílený kanál (PDSCH) pro přenos.
- Používá skupinové identifikátory, jako je G-RNTI, pro uživatelsky specifické dekódování sdíleného kanálu.
- Funguje bez zpětné vazby HARQ nebo retransmisí na vrstvě MAC.
- Je dynamicky konfigurován a plánován eNodeB na základě poptávky po službě.
- Je přidružen ke konkrétní vícebodové službě identifikované dočasným mobilním skupinovým identifikátorem (TMGI).

## Související pojmy

- [SC-PTM – Single-Cell Point-to-Multipoint](/mobilnisite/slovnik/sc-ptm/)
- [SC-MCCH – Single Cell Multicast Control Channel](/mobilnisite/slovnik/sc-mcch/)
- [SC-N-RNTI – Single Cell Notification RNTI](/mobilnisite/slovnik/sc-n-rnti/)
- [G-RNTI – GERAN Radio Network Temporary Identity](/mobilnisite/slovnik/g-rnti/)
- [MBSFN – Multimedia Broadcast multicast service Single Frequency Network](/mobilnisite/slovnik/mbsfn/)
- [MTCH – MBMS point-to-multipoint Traffic Channel](/mobilnisite/slovnik/mtch/)

## Definující specifikace

- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.322** (Rel-19) — E-UTRA Radio Link Control Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [SC-MTCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/sc-mtch/)
