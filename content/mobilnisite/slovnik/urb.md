---
slug: "urb"
url: "/mobilnisite/slovnik/urb/"
type: "slovnik"
title: "URB – User Radio Bearer"
date: 2025-01-01
abbr: "URB"
fullName: "User Radio Bearer"
category: "QoS"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/urb/"
summary: "Logický kanál zřízený přes rozhraní rádiového přenosu pro přenos dat uživatelské roviny pro konkrétní službu s definovanými charakteristikami kvality služby (QoS). Mapuje toky aplikačních dat na rádio"
---

URB je logický kanál přes rozhraní rádiového přenosu, který přenáší data uživatelské roviny pro konkrétní službu, mapuje aplikační toky na rádiové prostředky, aby splňoval definované požadavky na kvalitu služby (QoS).

## Popis

Uživatelský rádiový přenosový kanál (User Radio Bearer, URB) je základní koncept v 3GPP sítích rádiového přístupu, konkrétně v kontextu systémů GSM/[EDGE](/mobilnisite/slovnik/edge/) podle příslušných specifikací. Představuje logickou přenosovou cestu zřízenou přes rozhraní rádiového přenosu (rozhraní Um v GSM) mezi mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) a systémem základnových stanic ([BSS](/mobilnisite/slovnik/bss/)) za účelem přenosu dat uživatelské roviny. URB je podtypem rádiového přenosového kanálu (Radio Bearer), což je obecnější termín pro jakýkoli logický kanál přes rádiový spoj; předpona 'User' (uživatelský) jej odlišuje od signalizačních rádiových přenosových kanálů ([SRB](/mobilnisite/slovnik/srb/)), které přenášejí informace řídicí roviny.

URB funguje tak, že poskytuje vyhrazený logický kanál se specifickými atributy kvality služby (QoS) pro tok aplikačních dat uživatele, jako je například tok IP paketů pro prohlížení webu nebo hovor VoIP. Jeho zřízení je součástí procedur řízení rádiových prostředků. Když mobilní stanice zahájí datovou relaci, síť přiřadí jeden nebo více URB na základě požadovaného profilu QoS vyjednaného s jádrem sítě. URB je charakterizován parametry, jako je garantovaný přenosový výkon, maximální přenosový výkon, přenosové zpoždění a spolehlivost (míra chyb). Tyto parametry určují, jak nižší vrstvy – řídicí vrstva logického spoje ([LLC](/mobilnisite/slovnik/llc/)) a řídicí vrstva rádiového spoje ([RLC](/mobilnisite/slovnik/rlc/)) / řídicí vrstva přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) – s daty nakládají.

Z architektonického hlediska existuje URB jako logická asociace mezi protokolovými entitami v MS a BSS. V protokolovém zásobníku jsou uživatelská data z aplikační vrstvy zpracována IP vrstvou a následně zapouzdřena protokolem [SNDCP](/mobilnisite/slovnik/sndcp/) v GPRS. Tato datová jednotka SNDCP je pak namapována na jeden nebo více logických spojů LLC. URB je v podstatě rádiově specifická instance tohoto logického spoje pro daný dočasný blokový tok (TBF) v GPRS nebo pro kanál přenosu hovoru (TCH) v přepojovaných okruzích pro data. BSS je zodpovědný za plánování rádiových bloků (časových slotů) na fyzickém kanálu tak, aby splnil závazky QoS URB, provádí adaptaci spoje a spravuje opakované přenosy prostřednictvím protokolu RLC.

Role URB spočívá v tom, že izoluje vyšší vrstvy a aplikace od proměnlivosti rádiového média a zároveň dodává smluvně garantovanou kvalitu služby. Umožňuje síti poskytovat diferencované služby na stejných sdílených rádiových prostředcích. Například URB pro relaci online hry v reálném čase by byl nakonfigurován pro nízké zpoždění a rozkmity, zatímco URB pro stahování souboru na pozadí by byl nakonfigurován pro vysokou spolehlivost, ale toleroval by vyšší zpoždění. Správa URB – jejich zřizování, modifikace a uvolňování – je klíčovou funkcí správy rádiových prostředků v BSS a umožňuje efektivní multiplexování více uživatelů a služeb na omezeném rádiovém spektru.

## K čemu slouží

Koncept uživatelského rádiového přenosového kanálu (URB) byl zaveden, aby odstranil klíčovou nedostatečnost raných buněčných systémů: neschopnost efektivně podporovat různé datové služby s různými požadavky na kvalitu. Před-GPRS sítě GSM primárně nabízely přepojované okruhy s pevnou, neměnnou kvalitou (např. transparentní datový kanál 9,6 kbps). Tento 'univerzální' přístup byl neefektivní pro přerušované paketové datové přenosy a nemohl podporovat škálu vznikajících internetových aplikací, z nichž každá měla odlišné požadavky na šířku pásma, zpoždění a toleranci ztrát.

URB byl vytvořen jako součást vylepšení GPRS a později EDGE, aby umožnil skutečný paketově přepínaný mobilní přenos dat. Jeho účelem je poskytnout flexibilní transportní mechanismus přes rádiový spoj, který je vědomý kvality služby (QoS). Řeší problém mapování požadavků QoS, vyjednaných mezi aplikací mobilního uživatele a sítí (často prostřednictvím procedury aktivace PDP kontextu), na skutečné strategie přidělování a správy rádiových prostředků. Před zavedením URB neexistoval standardizovaný způsob, jak sdělit požadavky QoS specifické pro službu systému BSS pro dynamické plánování rádiových prostředků.

Historicky vycházela motivace z potřeby učinit sítě GSM konkurenceschopnými na vznikajícím datovém trhu a poskytnout migrační cestu ke službám 3G. Koncept URB umožnil operátorům nabízet datové služby v různých úrovních (např. prémiový vs. standardní přístup k internetu) a podporovat nové aplikace generující příjmy, jako je multimediální zasílání zpráv a mobilní e-mail. Položil základní kameny pro sofistikovanější koncept přenosového kanálu EPS (Evolved Packet System) používaný v LTE a 5G, který pokračuje v principu zřizování koncových kanálů s garantovanou QoS. URB tedy představuje klíčový evoluční krok v proměně buněčných sítí z čistých přenašečů hlasu na víceúčelové širokopásmové platformy.

## Klíčové vlastnosti

- Logický kanál vyhrazený pro přenos dat uživatelské roviny přes rozhraní rádiového přenosu
- Asociovaný se specifickou sadou parametrů QoS (přenosový výkon, zpoždění, spolehlivost)
- Dynamicky zřizovaný, modifikovaný a uvolňovaný na základě požadavků služby
- Mapuje toky paketů z vyšších vrstev (např. IP toky) na rádiové prostředky (časové sloty/TBF)
- Spravován systémem základnových stanic (BSS) pro efektivní plánování rádiových prostředků
- Podporuje diferencované zacházení s datovým provozem, aby umožnil více souběžných služeb

## Související pojmy

- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 44.160** (Rel-16) — GERAN Iu Mode RLC/MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [URB na 3GPP Explorer](https://3gpp-explorer.com/glossary/urb/)
