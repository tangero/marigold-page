---
slug: "tftp"
url: "/mobilnisite/slovnik/tftp/"
type: "slovnik"
title: "TFTP – Trivial File Transfer Protocol"
date: 2026-01-01
abbr: "TFTP"
fullName: "Trivial File Transfer Protocol"
category: "Protocol"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/tftp/"
summary: "Jednoduchý, lock-step protokol pro přenos souborů používaný v sítích 3GPP pro stahování konfiguračních souborů, softwarových aktualizací a hromadných dat na síťové prvky a uživatelská zařízení. Poskyt"
---

TFTP je jednoduchý, lock-step protokol pro přenos souborů využívající UDP, který poskytuje odlehčenou metodu pro stahování konfiguračních souborů, softwarových aktualizací a hromadných dat na síťové prvky a uživatelská zařízení v sítích 3GPP.

## Popis

Trivial File Transfer Protocol (TFTP) je zjednodušený protokol pro přenos souborů standardizovaný v rámci 3GPP pro specifické operace správy a provizionování. Na rozdíl od složitějšího File Transfer Protocol ([FTP](/mobilnisite/slovnik/ftp/)) používá TFTP jako transportní vrstvu [UDP](/mobilnisite/slovnik/udp/) (User Datagram Protocol), typicky na portu 69, a využívá lock-step mechanismus založený na potvrzeních pro přenos dat. Je navržen jako malý a snadno implementovatelný, což jej činí vhodným pro vestavění do firmware nebo zavaděčů síťových prvků a uživatelských zařízení s omezenými prostředky. Protokol funguje v modelu klient-server, kdy klient zahájí požadavek na čtení nebo zápis na serveru. Přenos probíhá v blocích pevné velikosti (standardně 512 bajtů), přičemž každý blok musí být potvrzen před odesláním dalšího. Přenos končí při přijetí datového bloku menšího než 512 bajtů, což signalizuje konec souboru.

V rámci architektury 3GPP je TFTP primárně specifikován pro doménu [OAM](/mobilnisite/slovnik/oam/) (Operations, Administration, and Maintenance). Používají jej systémy správy, jako je Element Management System ([EMS](/mobilnisite/slovnik/ems/)) nebo Network Management System ([NMS](/mobilnisite/slovnik/nms/)), k nasazení konfiguračních souborů, softwarových balíčků nebo aktualizací firmware na síťové uzly, jako jsou základnové stanice (eNodeB/gNB) nebo funkce jádra sítě. Je také využíván ve scénářích správy zařízení, například v kontextu Open Mobile Alliance Device Management ([OMA](/mobilnisite/slovnik/oma/) [DM](/mobilnisite/slovnik/dm/)) nebo pro provizionování parametrů v zařízeních pro Machine-Type Communication ([MTC](/mobilnisite/slovnik/mtc/)). Jednoduchost protokolu snižuje zátěž spravovaných zařízení, která mohou mít omezený výpočetní výkon nebo paměť.

Klíčové komponenty transakce TFTP zahrnují pakety RRQ (Read Request) a WRQ (Write Request), DATA pakety obsahující bloky souboru a ACK (Acknowledgment) pakety. Ošetření chyb je zajištěno prostřednictvím ERROR paketů. Kvůli své bezspojové povaze nad UDP TFTP inherentně neposkytuje bezpečnostní funkce jako autentizaci nebo šifrování; tyto aspekty musí být řešeny na vyšší vrstvě nebo v aplikaci, která jej používá. V 3GPP je jeho použití často řízeno bezpečnostními specifikacemi, které vyžadují zabezpečené transportní kanály (např. IPsec) nebo ochranu integrity přenášených souborů. Jeho role je zásadní pro zero-touch provizionování, vzdálené softwarové aktualizace a hromadnou konfiguraci síťových prvků, což umožňuje efektivní a automatizovanou správu sítě.

## K čemu slouží

TFTP byl zaveden, aby uspokojil potřebu jednoduchého, standardizovaného mechanismu pro přenos souborů na síťové prvky a uživatelská zařízení a z nich v rámci automatizovaných workflow provizionování a správy. Před jeho formálním přijetím v 3GPP se používaly proprietární metody nebo složitější protokoly jako FTP, které mohly být náročné na prostředky nebo vyžadovaly plné TCP/IP zásobníky. Minimalistický návrh TFTP umožňuje jeho implementaci v prostředích s omezenými výpočetními zdroji, jako je boot ROM zařízení nebo odlehčený správní agent na síťovém uzlu.

Historický kontext spočívá v automatizaci provozu telekomunikačních sítí. Jak sítě rostly ve velikosti a složitosti, ruční konfigurace každé základnové stanice nebo prvku jádra sítě se stala nepraktickou. Byl potřeba protokol pro spolehlivé vzdálené nasazování konfiguračních souborů, softwarových záplat a firmware obrazů. TFTP se svým dobře definovaným IETF RFC (původně RFC 783, později RFC 1350) a jednoduchostí tuto roli splnil. Řeší problém hromadného, skriptovatelného distribuce souborů pro účely správy. Jeho použití nad UDP, ačkoli méně spolehlivé než TCP, je přijatelné v řízených správních sítích a umožňuje přímočarou implementaci a nízkou režii, což je klíčové během fází bootstrapu zařízení nebo v IoT zařízeních s omezenými prostředky.

## Klíčové vlastnosti

- Transport založený na UDP pro jednoduchost a nízkou režii
- Lock-step mechanismus potvrzování pro spolehlivý přenos bloků
- Podpora operací čtení a zápisu souborů
- Přenos datových bloků pevné velikosti (typicky 512 bajtů)
- Minimální nároky protokolu vhodné pro vestavěné systémy
- Definované signalizování chyb prostřednictvím ERROR paketů

## Související pojmy

- [EMS – Enhanced Messaging Service](/mobilnisite/slovnik/ems/)
- [NMS – Network Management Subsystem](/mobilnisite/slovnik/nms/)
- [IPSec – Internet Protocol Security](/mobilnisite/slovnik/ipsec/)

## Definující specifikace

- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- **TS 32.406** (Rel-19) — Performance Management for CN PS Domain
- **TS 33.117** (Rel-20) — Catalogue of General Security Assurance Requirements
- **TR 37.901** (Rel-15) — UE Application Layer Data Throughput Performance

---

📖 **Anglický originál a plná specifikace:** [TFTP na 3GPP Explorer](https://3gpp-explorer.com/glossary/tftp/)
