---
slug: "san"
url: "/mobilnisite/slovnik/san/"
type: "slovnik"
title: "SAN – Satellite Access Node"
date: 2025-01-01
abbr: "SAN"
fullName: "Satellite Access Node"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/san/"
summary: "Síťový uzel v neterestrické síti (NTN), který poskytuje radiový přístup uživatelskému zařízení (UE) prostřednictvím satelitu. Zahrnuje funkce pro rádiový přenos/příjem a může být integrován s základno"
---

SAN je síťový uzel v neterestrické síti (NTN), který poskytuje radiový přístup uživatelskému zařízení prostřednictvím satelitu. Zahrnuje rádiové funkce a může být integrován s pozemním gNB nebo k němu přenášet signály.

## Popis

Satellite Access Node (SAN) je základní součást neterestrických sítí ([NTN](/mobilnisite/slovnik/ntn/)) definovaných 3GPP, zavedený k formalizaci integrace satelitního přístupu do systému 5G. Koncepčně je SAN satelitní entita implementující rádiové rozhraní směrem k uživatelskému zařízení (UE). Jeho konkrétní architektura a funkční rozdělení se mohou lišit, což vede ke dvěma hlavním implementacím: modelu 'gNB-on-satellite' (regenerativní) a modelu 'satelit jako retranslátor' (transparentní).

V regenerativním modelu SAN obsahuje celý protokolový zásobník gNB (Next Generation NodeB), včetně vrstev [RRC](/mobilnisite/slovnik/rrc/) (Radio Resource Control), [PDCP](/mobilnisite/slovnik/pdcp/) (Packet Data Convergence Protocol), [RLC](/mobilnisite/slovnik/rlc/) (Radio Link Control), [MAC](/mobilnisite/slovnik/mac/) (Medium Access Control) a [PHY](/mobilnisite/slovnik/phy/) (Physical). V této architektuře satelit funguje jako plnohodnotná základnová stanice ve vesmíru. Demoduluje, dekóduje, zpracovává a znovu kóduje uplinkové signály před jejich přenosem k pozemní bráně nebo k jádru sítě. Tím se snižuje latence na feeder lince mezi satelitem a zemí, ale vyžaduje to větší výpočetní výkon na satelitu.

V transparentním (nebo 'bent-pipe') modelu SAN funguje primárně jako rádiový frekvenční ([RF](/mobilnisite/slovnik/rf/)) retranslátor. Přijímá RF signál od UE na uplinku, provádí frekvenční konverzi a zesílení a retransluje jej směrem k pozemnímu gNB. V tomto případě je gNB umístěn na Zemi a SAN nezpracovává basebandové protokoly. Charakteristiky SAN, jako je jeho oběžná dráha ([GEO](/mobilnisite/slovnik/geo/), MEO, LEO), tvar pokrytí paprskem a zpoždění šíření, jsou klíčové parametry, kterým se musí přizpůsobit 5G NR rozhraní a protokoly. Klíčové specifikace jako TS 38.108 definují požadavky na rádiový přenos a příjem pro SAN, zatímco požadavky na výkon jsou pokryty specifikacemi jako TS 38.101 a TS 38.521.

## K čemu slouží

Standardizace SAN řeší rostoucí potřebu rozšířit pokrytí 5G do nedostatečně pokrytých oblastí, kde je nasazení terestrické infrastruktury ekonomicky nebo geograficky náročné, jako jsou oceány, pouště a odlehlé venkovské regiony. Před prací 3GPP na NTN fungovaly satelitní komunikační systémy z velké části nezávisle na celulárních standardech, vyžadovaly dvou režimová zařízení a postrádaly bezproblémovou integraci služeb. Koncept SAN poskytuje standardizovaný rámec, díky kterému může být satelitní přístup přirozenou součástí ekosystému 3GPP.

Jeho vytvoření, zejména ve verzi 17 (Release 17), bylo motivováno globálními iniciativami pro všudypřítomnou konektivitu a odolnost vůči katastrofám. Řeší problém definice přístupového uzlu ve vesmíru specifikací funkčních požadavků a rozhraní, což umožňuje satelitním operátorům stavět kompatibilní přenosové jednotky a výrobcům zařízení podporovat NTN konektivitu. Definováním chování SAN a nezbytných úprav v protokolovém zásobníku NR (např. pro dlouhé zpoždění, vysoký Doppler) 3GPP zajišťuje, že standardní UE se může s minimálními úpravami připojit k satelitní síti, což podporuje sjednocený trh pro zařízení a služby.

## Klíčové vlastnosti

- Poskytuje rádiové rozhraní pro UE v neterestrické síti (NTN)
- Může být implementován jako regenerativní přenosová jednotka (gNB-on-satellite) nebo transparentní přenosová jednotka (RF retranslátor)
- Definované charakteristiky rádiového přenosu a příjmu (např. EIRP, G/T)
- Podporuje různé satelitní oběžné dráhy (GEO, MEO, LEO) s odpovídajícími profily Dopplerova jevu a zpoždění
- Integruje se s jádrem sítě 5G prostřednictvím feeder linky a brány
- Podléhá specifickým požadavkům na RF výkon definovaným ve specifikacích 3GPP

## Související pojmy

- [NTN – Non-Terrestrial Networks](/mobilnisite/slovnik/ntn/)

## Definující specifikace

- **TR 33.876** (Rel-18) — Technical Report on Certificate Management
- **TS 36.108** (Rel-19) — Satellite Access Node RF Requirements
- **TS 36.181** (Rel-19) — E-UTRA RF Test Methods for Satellite Access Node
- **TS 36.214** (Rel-19) — E-UTRA Physical Layer Measurements
- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.108** (Rel-19) — NTN NR Satellite Access Node RF Requirements
- **TS 38.181** (Rel-19) — NR Satellite Access Node RF Testing
- **TS 38.521** (Rel-19) — NR Physical Layer UE Conformance Testing
- **TS 38.741** (Rel-19) — NTN L-/S-band for NR Technical Specification
- **TS 38.762** (Rel-19) — Dynamic MIMO OTA Test Methodology for NR FR1
- **TS 38.863** (Rel-19) — NR NTN RF and Co-existence Spec

---

📖 **Anglický originál a plná specifikace:** [SAN na 3GPP Explorer](https://3gpp-explorer.com/glossary/san/)
