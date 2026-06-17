---
slug: "ec-agch"
url: "/mobilnisite/slovnik/ec-agch/"
type: "slovnik"
title: "EC-AGCH – Extended Coverage Access Grant CHannel"
date: 2025-01-01
abbr: "EC-AGCH"
fullName: "Extended Coverage Access Grant CHannel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ec-agch/"
summary: "Logický kanál v sítích GSM/EDGE, specificky vylepšený pro provoz v režimu rozšířeného pokrytí (EC). Síť jej používá k udělení přístupu mobilní stanici (MS), která o prostředky požádala, a to zejména v"
---

EC-AGCH je logický kanál v sítích GSM/EDGE, vylepšený pro rozšířené pokrytí (Extended Coverage), který síť používá k přidělení přístupu k prostředkům mobilní stanici, zejména v obtížných rádiových podmínkách pro zařízení IoT.

## Popis

EC-AGCH (Extended Coverage Access Grant CHannel) je downlinkový logický kanál definovaný v architektuře GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)), specifikovaný v 3GPP TS 44.060. Jedná se o specializovanou verzi standardního kanálu [AGCH](/mobilnisite/slovnik/agch/), optimalizovanou pro provoz v rámci funkce rozšířeného pokrytí ([EC](/mobilnisite/slovnik/ec/)), která je určena pro komunikaci typu Machine-Type Communication ([MTC](/mobilnisite/slovnik/mtc/)) a zařízení Internetu věcí (IoT). Jako logický kanál se nachází na vrstvě řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) a je mapován na fyzické prostředky. Jeho hlavní funkcí je přenos zprávy Immediate Assignment ze sítě ([BSS](/mobilnisite/slovnik/bss/)) k mobilní stanici ([MS](/mobilnisite/slovnik/ms/)), která předtím odeslala žádost o kanál na RACH nebo EC-RACH.

Operačně, když MS v režimu EC zahájí transakci, odešle přístupový vzruch na náhodný přístupový kanál (RACH nebo EC-RACH). Systém základnových stanic (BSS) tuto žádost přijme a pokud jsou prostředky k dispozici, odpoví zprávou Immediate Assignment na EC-AGCH. Tato zpráva instruuje MS, který vyhrazený kanál pro přenos hovoru nebo datový kanál má použít pro následnou komunikaci. Klíčovým technickým vylepšením EC-AGCH oproti standardnímu AGCH je podpora rozsáhlého opakovacího kódování. Pro dosažení potřebného útlumu na trase pro hluboké pokrytí (až o 20 dB nad rámec běžného pokrytí GSM) jsou zprávy na EC-AGCH přenášeny s mnoha opakováními přes několik rádiových bloků, což přijímači umožňuje je kombinovat a úspěšně dekódovat i při velmi nízkých úrovních signálu.

Návrh kanálu je nedílnou součástí systému EC-GSM-IoT. Spolupracuje s dalšími EC kanály (EC-BCCH, EC-CCCH) a vytváří tak řídicí rovinu schopnou obsluhovat zařízení ve sklepeních, hluboko uvnitř budov nebo v odlehlých oblastech. Síť plánuje přenosy na EC-AGCH podle předdefinovaného vzoru a MS musí sledovat příslušné časové sloty. Jeho spolehlivý provoz je základním předpokladem pro přístup k síti v režimu EC, zajišťuje, že zařízením mohou být přiděleny prostředky pro navázání spojení, ať už pro přenos malých objemů dat, aktualizace polohy nebo jiné řídicí procedury, čímž naplňuje požadavky na masivní, nízkonákladová a hluboce pokrývající nasazení IoT.

## K čemu slouží

EC-AGCH byl vytvořen k řešení kritického problému poskytování spolehlivého signalizačního kanálu pro udělení přístupu k síti zařízením IoT a MTC pracujícím v extrémně náročných rádiových podmínkách. Před 3GPP Release 13 a standardizací EC-GSM-IoT byly standardní GSM kanály, jako AGCH, nedostatečné pro zařízení umístěná hluboko uvnitř budov nebo v odlehlých oblastech, například vodoměry ve sklepích nebo zemědělské senzory ve venkovských lokalitách. Standardním kanálům chyběla potřebná rezerva útlumu na trase a robustnost, což vedlo k neúspěšným pokusům o přístup a nespolehlivosti služby pro tyto případy použití s nízkou spotřebou a širokou oblastí pokrytí.

Motivace vycházela z potřeby průmyslu po technologii celulárního IoT, která by dokázala využít všudypřítomnou GSM infrastrukturu a zároveň nabídnout výrazně lepší pokrytí. EC-AGCH jako součást sady funkcí EC-GSM-IoT řeší omezení předchozího přístupu zavedením masivního opakování řídicích zpráv. To umožňuje časovou integraci signálu, efektivně jej 'vyhrabat' z šumu a poskytnout až 20 dB dodatečné rezervy pro ztrátu na trase. Jeho existence zajišťuje, že odpověď sítě na pokus o přístup – klíčový krok při navazování spojení – je stejně robustní jako samotný počáteční přístupový požadavek, čímž vytváří vyvážený a spolehlivý přenosový kanál pro řídicí signalizaci ve scénářích s rozšířeným pokrytím.

## Klíčové vlastnosti

- Přenáší zprávu Immediate Assignment pro přidělení prostředků v režimu EC
- Využívá rozsáhlé opakovací kódování (přes více rádiových bloků) pro hluboké pokrytí
- Funguje jako downlinkový logický kanál v rámci architektury GERAN
- Specificky navržen pro komunikaci v systému EC-GSM-IoT a pro zařízení MTC
- Spolupracuje s EC-RACH pro kompletní přístupovou proceduru v obtížných podmínkách
- Umožňuje spolehlivý přístup k síti zařízením s až o 20 dB vyšší ztrátou na trase

## Související pojmy

- [EC-RACH – Extended Coverage Random Access Channel](/mobilnisite/slovnik/ec-rach/)
- [EC-BCCH – Extended Coverage BroadCast CHannel](/mobilnisite/slovnik/ec-bcch/)
- [EC-CCCH – Extended Coverage Common Control CHannel](/mobilnisite/slovnik/ec-ccch/)
- [AGCH – Access Grant Channel](/mobilnisite/slovnik/agch/)

## Definující specifikace

- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [EC-AGCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/ec-agch/)
