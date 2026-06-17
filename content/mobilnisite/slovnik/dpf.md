---
slug: "dpf"
url: "/mobilnisite/slovnik/dpf/"
type: "slovnik"
title: "DPF – Direct Services Provisioning Function"
date: 2026-01-01
abbr: "DPF"
fullName: "Direct Services Provisioning Function"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dpf/"
summary: "Funkce přímého poskytování služeb (Direct Services Provisioning Function, DPF) je síťová funkce, která umožňuje přímé poskytování služeb uživatelskému zařízení (UE), aniž by toto zařízení muselo být p"
---

DPF je síťová funkce, která umožňuje přímé poskytování služeb uživatelskému zařízení (User Equipment), aniž by toto zařízení muselo být připojeno k síti 3GPP pro signalizaci v řídicí rovině.

## Popis

Funkce přímého poskytování služeb (DPF) je logická funkce, která usnadňuje doručování služeb uživatelskému zařízení (UE), zejména takovému, které je nakonfigurováno pro režim úspory energie (Power Saving Mode, PSM) nebo rozšířený nepřetržitý příjem v nečinnosti (eDRX), prostřednictvím rozhraní s jádrem sítě. Působí jako koncový bod aplikační vrstvy, který může přijímat datové toky směrem dolů nebo požadavky na spouštění od externího serveru schopností služeb (SCS) nebo aplikačního serveru ([AS](/mobilnisite/slovnik/as/)). Když taková data dorazí pro UE, které není dosažitelné běžným vyhledáváním (např. v PSM), DPF tato data uloží a spojí je s událostí spuštění.

Architektonicky může být DPF implementována jako součást serveru schopností služeb (SCS) v rámci frameworku pro vystavení sítě 3GPP nebo jako samostatná entita. Komunikuje s funkcí pro vystavení schopností služeb (SCEF) v jádru sítě 4G nebo s funkcí pro vystavení sítě ([NEF](/mobilnisite/slovnik/nef/)) v jádru sítě 5G. Klíčová operace spočívá v tom, že DPF požádá síť o provedení procedury spouštění zařízení (Device Triggering). Odešle zprávu žádosti o spuštění zařízení (Device Trigger Request) do SCEF/NEF, která ji pak přepošle na entitu správy mobility ([MME](/mobilnisite/slovnik/mme/)) v 4G nebo na funkci správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) v 5G. Síť se pak pokusí doručit notifikaci ne-přístupové vrstvy ([NAS](/mobilnisite/slovnik/nas/)) nebo službu krátkých textových zpráv (SMS) do UE, aby je vyzvala k opětovnému připojení a navázání datového spojení pro získání čekajících dat.

Princip fungování zahrnuje mechanismus uložení a upozornění. DPF uchovává datové toky směrem dolů nebo servisní příkazy. Poté použije službu spouštění zařízení k odeslání malého signálu pro probuzení (spouštěče) do UE prostřednictvím signalizačních cest jádra sítě. Tento spouštěč obsahuje jen dostatek informací k instruování UE, aby zahájilo proceduru iniciovanou mobilním zařízením ([MO](/mobilnisite/slovnik/mo/)). Jakmile se UE připojí, může kontaktovat svou aplikační platformu (která může být umístěna společně s DPF nebo k ní připojena), aby si stáhla čekající data. Tento model obrací klasický model 'vždy připojeného' doručování směrem dolů a optimalizuje životnost baterie zařízení IoT.

## K čemu slouží

DPF byla vytvořena k řešení kritického problému v komunikaci typu stroj-stroj ([MTC](/mobilnisite/slovnik/mtc/)) a internetu věcí (IoT): jak odeslat data zařízení, které je v hlubokém režimu úspory energie pro maximalizaci životnosti baterie. Tradiční mobilní sítě vyžadují, aby bylo zařízení periodicky dosažitelné pro vyhledávání, aby mohlo přijímat data směrem dolů. Režim úspory energie (PSM) a eDRX, zavedené pro IoT, tento model narušují tím, že umožňují zařízením spát po velmi dlouhá období, čímž je činí nedosažitelnými pro provoz směrem dolů. DPF poskytuje mechanismus k 'probuzení' takových zařízení efektivním způsobem z hlediska sítě.

Řeší omezení předchozích přístupů, kdy jedinou možností bylo čekat, až se zařízení probudí podle vlastního plánu (pouze provoz iniciovaný mobilním zařízením), nebo používat trvalá spojení, která vybíjejí baterii. DPF umožňuje 'síťově iniciovaný' model služeb, který je nezbytný pro mnoho IoT aplikací, jako jsou aktualizace firmwaru, příkazy dálkového ovládání nebo potvrzení alarmů, které musí být iniciovány ze strany sítě.

Její vývoj a standardizace v 3GPP (počínaje Release 9 a vylepšená v pozdějších vydáních) byly motivovány projekcemi masivního rozsahu IoT. DPF, jako součást širší sady funkcí pro komunikaci typu stroj-stroj (MTC) a celulární IoT (CIoT), umožňuje operátorům nabízet efektivní a škálovatelné služby pro miliony zařízení s nízkou spotřebou. Usnadňuje nové obchodní modely a aplikace, kde zařízení mohou zůstat v nečinnosti roky, ale zůstávají reagující na kritické příkazy iniciované sítí.

## Klíčové vlastnosti

- Umožňuje doručování dat směrem dolů a spouštění služeb pro UE v režimech úspory energie (PSM, eDRX)
- Komunikuje s funkcemi pro vystavení jádra sítě (SCEF v 4G, NEF v 5G) pro spouštění zařízení (Device Triggering)
- Ukládá datové toky směrem dolů nebo servisní příkazy čekající na dostupnost zařízení
- Iniciuje notifikace ne-přístupové vrstvy (NAS) nebo probouzející signály založené na SMS pro UE
- Klíčová součást architektur MTC a CIoT podle 3GPP pro efektivní komunikaci iniciovanou sítí
- Podporuje model služeb 'Mobile Terminated' pro zařízení IoT s omezenou kapacitou baterie

## Související pojmy

- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)

## Definující specifikace

- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.303** (Rel-19) — Proximity Services (ProSe) Stage 2
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 24.333** (Rel-19) — ProSe Management Objects for UE Configuration
- **TS 32.844** (Rel-12) — Charging for ProSe Direct Communication in Public Safety
- **TS 33.812** (Rel-9) — M2M Remote Subscription Management Security

---

📖 **Anglický originál a plná specifikace:** [DPF na 3GPP Explorer](https://3gpp-explorer.com/glossary/dpf/)
