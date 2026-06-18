---
slug: "imei-sv"
url: "/mobilnisite/slovnik/imei-sv/"
type: "slovnik"
title: "IMEI-SV – International Mobile Equipment Identity Software Version"
date: 2025-01-01
abbr: "IMEI-SV"
fullName: "International Mobile Equipment Identity Software Version"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/imei-sv/"
summary: "16místné rozšíření IMEI obsahující dvoumístné číslo verze softwaru. Identifikuje konkrétní verzi softwaru/firmwaru nainstalovanou na mobilním zařízení a napomáhá správě zařízení a sledování softwarový"
---

IMEI-SV je 16místné rozšíření IMEI, které obsahuje dvoumístné číslo verze softwaru pro identifikaci konkrétní softwarové verze na mobilním zařízení za účelem správy a sledování aktualizací.

## Popis

International Mobile Equipment Identity Software Version (IMEI-SV) je rozšířený identifikátor, který vychází ze standardního [IMEI](/mobilnisite/slovnik/imei/). Jedná se o 16místné číslo, kde prvních 14 číslic je shodných s IMEI (8místný [TAC](/mobilnisite/slovnik/tac/) a 6místný [SNR](/mobilnisite/slovnik/snr/), bez kontrolní číslice IMEI). Poslední dvě číslice představují Software Version Number ([SVN](/mobilnisite/slovnik/svn/)), které identifikuje revizi softwaru nebo firmwaru aktuálně nainstalovaného na zařízení. To umožňuje rozlišit různé softwarové sestavy běžící na stejném modelu hardwaru.

Zařízení hlásí IMEI-SV síti podobným způsobem jako IMEI, typicky během počáteční registrace nebo na vyžádání sítě. V systémech LTE a 5G může zařízení hlásit jak IMEI, tak IMEI-SV. Síť, konkrétně systémy správy a Equipment Identity Register ([EIR](/mobilnisite/slovnik/eir/)), může informaci o SVN zpracovávat. To umožňuje podrobnější identifikaci zařízení. Například operátor může určit nejen model zařízení (pomocí TAC), ale také to, zda na něm běží konkrétní, potenciálně zranitelná nebo nekompatibilní, verze softwaru.

Primární technickou úlohou IMEI-SV je podpora pokročilé správy zařízení a bezpečnostních operací. V kontextu Over-The-Air ([OTA](/mobilnisite/slovnik/ota/)) softwarových aktualizací může síť nebo výrobce zařízení ověřit aktuální softwarovou verzi cílového zařízení před zahájením aktualizace. Při reakci na bezpečnostní incidenty, pokud je zranitelnost objevena v konkrétní softwarové verzi, mohou operátoři pomocí dat IMEI-SV identifikovat a potenciálně izolovat postižená zařízení ve své síti. Také napomáhá při řešení problémů a zákaznické podpoře tím, že poskytuje přesné informace o softwarovém stavu zařízení nad rámec jeho hardwarové identity. SVN je typicky přidělováno a spravováno výrobcem zařízení.

## K čemu slouží

IMEI-SV bylo zavedeno jako odpověď na rostoucí složitost mobilních zařízení, kde se software/firmware stal pro funkčnost a bezpečnost zařízení stejně kritický jako hardware. Standardní [IMEI](/mobilnisite/slovnik/imei/) identifikovalo pouze fyzický hardware, což znemožňovalo sítím rozlišit mezi dvěma stejnými modely telefonů s různými verzemi OS nebo firmware. Toto bylo významným omezením pro implementaci softwarově založených bezpečnostních politik, správu kampaní aktualizací firmwaru a reakci na softwarově specifické zranitelnosti nebo chyby.

Před zavedením IMEI-SV měli síťoví operátoři a výrobci omezený přehled o softwarové krajině zařízení ve svých sítích. Vytvoření IMEI-SV, standardizovaného v 3GPP Release 11, poskytlo standardizovaný mechanismus pro vložení informace o verzi softwaru přímo do známého identifikátoru zařízení. Tím byl vyřešen problém korelace identity zařízení s jeho softwarovým stavem, což umožnilo přesné cílení softwarových aktualizací, usnadnilo kontrolu souladu (např. ověření, že zařízení má povinnou bezpečnostní záplatu) a zvýšilo schopnost bezpečnostních systémů jednat na základě známých softwarových zranitelností přítomných v konkrétních rozsazích [SVN](/mobilnisite/slovnik/svn/).

## Klíčové vlastnosti

- 16místný identifikátor rozšiřující formát IMEI
- Obsahuje dvoumístné Software Version Number (SVN)
- Jednoznačně identifikuje model hardwaru zařízení a revizi softwaru
- Umožňuje síťové povědomí o verzi softwaru
- Podporuje cílenou správu a nasazení aktualizací firmwaru
- Napomáhá bezpečnostní reakci na softwarově specifické zranitelnosti

## Související pojmy

- [IMEI – International Mobile Station Equipment Identities](/mobilnisite/slovnik/imei/)
- [IMEI-TAC – Type Allocation Code part of an IMEI](/mobilnisite/slovnik/imei-tac/)
- [SVN – Satellite Virtual Network](/mobilnisite/slovnik/svn/)

## Definující specifikace

- **TS 37.320** (Rel-19) — Minimization of Drive Tests (MDT) Overview

---

📖 **Anglický originál a plná specifikace:** [IMEI-SV na 3GPP Explorer](https://3gpp-explorer.com/glossary/imei-sv/)
