---
slug: "mo-edt"
url: "/mobilnisite/slovnik/mo-edt/"
type: "slovnik"
title: "MO-EDT – Mobile Originated Early Data Transmission"
date: 2026-01-01
abbr: "MO-EDT"
fullName: "Mobile Originated Early Data Transmission"
category: "Radio Access Network"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/mo-edt/"
summary: "MO-EDT je funkce pro Narrowband IoT (NB-IoT) a LTE-M, která umožňuje zařízení přenést malé množství dat v uplinku během procedury náhodného přístupu, před plným navázáním RRC spojení. Výrazně snižuje"
---

MO-EDT je funkce pro NB-IoT a LTE-M, kdy zařízení odešle malé množství dat v uplinku již na začátku procedury náhodného přístupu, před plným navázáním spojení, aby se snížila signalizace, latence a spotřeba energie.

## Popis

Mobile Originated Early Data Transmission (MO-EDT, časný přenos dat iniciovaný mobilním zařízením) je optimalizační mechanismus definovaný pro technologie Cellular IoT (CIoT), konkrétně NB-IoT a LTE-M (eMTC). Umožňuje UE odeslat omezenou uživatelskou datovou náplň v uplinku zabudovanou do Msg3 procedury Random Access Channel ([RACH](/mobilnisite/slovnik/rach/)) v LTE nebo do zprávy [RRC](/mobilnisite/slovnik/rrc/) Early Data Request v NR, než se spojení Radio Resource Control (RRC) přepne do stavu RRC_CONNECTED. Tento proces obchází kompletní navázání spojení, které zahrnuje více signalizačních zpráv pro aktivaci zabezpečení a zřízení datového rádiového přenosového kanálu.

Procedura je zahájena, když CIoT UE ve stavu RRC_IDLE nebo RRC_INACTIVE má k odeslání malé množství dat (až několik set bajtů, jak definuje síť). UE oznámí svou schopnost a záměr použít [EDT](/mobilnisite/slovnik/edt/) v preambuli náhodného přístupu (Msg1) nebo v RRC Connection Request (Msg3). Síť, pokud EDT podporuje, odpoví zprávou (např. [RAR](/mobilnisite/slovnik/rar/) pro Msg2 nebo RRC Connection Setup for EDT), která přiděluje zdroje a parametry pro přenos dat v uplinku. UE poté přenese svá data spolu s RRC zprávou (např. RRC Early Data Request) na přidělených uplinkových zdrojích.

Mezi klíčové komponenty patří CIoT zásobník UE, eNodeB/gNodeB, který musí podporovat zpracování EDT, a jádro sítě ([MME](/mobilnisite/slovnik/mme/) pro LTE, [AMF](/mobilnisite/slovnik/amf/) pro 5GC). Uzel jádra sítě přijímá data prostřednictvím zprávy S1-AP nebo [NG-AP](/mobilnisite/slovnik/ng-ap/) Initial UE Message, která nese uživatelskou datovou náplň. Po úspěšném přijetí může síť RRC spojení okamžitě uvolnit, aniž by převedla UE do stavu RRC_CONNECTED, a to odesláním uvolňovací zprávy (např. RRC Connection Release), která může v případě potřeby obsahovat malou downlinkovou odpověď. Celá tato výměna je obsažena ve fázích signalizace náhodného přístupu a počátečního spojení.

Úloha MO-EDT v síti spočívá v minimalizaci signalizační režie a spotřeby energie spojené s občasnými přenosy malých objemů dat, což je charakteristické pro mnoho IoT aplikací, jako jsou odečty senzorů nebo aktualizace stavu. Snížením počtu vyměněných zpráv a doby, po kterou je rádio aktivní, prodlužuje životnost baterie zařízení, která mohou být nasazena na roky. Jedná se o klíčový prvek pro use case masové komunikace mezi stroji (mMTC) v rámci 5G, který zlepšuje efektivitu sítě snížením zahlcení řídicí roviny.

## K čemu slouží

MO-EDT byl vytvořen, aby řešil výraznou neefektivitu používání tradičních procedur navazování spojení LTE pro IoT zařízení, která potřebují odesílat pouze velmi malé, občasné datové pakety. Standardní navázání [RRC](/mobilnisite/slovnik/rrc/) spojení v LTE zahrnuje několik výměn zpráv (RRC Connection Request, Setup, Complete, Security Mode Command atd.), z nichž každá vyžaduje energii zařízení a síťové zdroje. Pro senzor odesílající několik bajtů dat by tato signalizační režie mohla být řádově větší než samotná datová náplň, což vede ke špatné životnosti baterie a zbytečné zátěži sítě.

Tato technologie řeší problém optimalizace síťové architektury pro masivní nasazení IoT s nízkým výkonem a nízkou přenosovou rychlostí. Byla motivována požadavky pracovní položky Cellular IoT v 3GPP, jejímž cílem bylo umožnit životnost baterie zařízení přes 10 let. Předchozí přístupy, jako je Power Saving Mode (PSM) a rozšířené nespojité příjímání (eDRX), pomáhaly s úsporou energie v režimu nečinnosti, ale nesnižovaly signalizační náklady na přenos.

MO-EDT, zavedený ve vydání 15/16, se tímto problémem zabývá přímo tím, že umožňuje přenos dat během počátečního přístupu, čímž efektivně slučuje přenos dat s fází žádosti o spojení. Tím se snižuje latence, počet signalizačních zpráv a doba zapnutého rádia, což přímo vede k nižší spotřebě energie. Představuje posun v designové filozofii, který zachází s malými daty jako s nedílnou součástí řídicí procedury, nikoli jako se samostatnou aktivitou uživatelské roviny.

## Klíčové vlastnosti

- Uplinková data v Msg3/RRC Request: Přenáší uživatelskou datovou náplň uvnitř zprávy RRC Connection Request nebo Early Data Request během náhodného přístupu.
- Žádné plné RRC spojení: Vyhýbá se přechodu do stavu RRC_CONNECTED, přeskočí aktivaci zabezpečení a zřízení datového rádiového přenosového kanálu pro tento přenos.
- Rychlé uvolnění: Síť může spojení okamžitě uvolnit po přijetí dat pomocí zprávy RRC Connection Release.
- Omezená velikost náplně: Podporuje přenos malých datových paketů (velikost definovaná sítí, typicky až ~1000 bajtů pro LTE-M, méně pro NB-IoT).
- Podpora downlinkové odpovědi: Umožňuje síti zahrnout malou downlinkovou datovou odpověď do zprávy o uvolnění spojení.
- Provoz ve stavech IDLE/INACTIVE: Může být zahájen ze stavů RRC_IDLE (LTE) i RRC_INACTIVE (5G NR), což odpovídá stavům pro úsporu energie u IoT.

## Související pojmy

- [RACH – Random Access Channel](/mobilnisite/slovnik/rach/)

## Definující specifikace

- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.306** (Rel-19) — E-UTRA UE Radio Access Capability Parameters

---

📖 **Anglický originál a plná specifikace:** [MO-EDT na 3GPP Explorer](https://3gpp-explorer.com/glossary/mo-edt/)
