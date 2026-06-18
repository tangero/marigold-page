---
slug: "tnla"
url: "/mobilnisite/slovnik/tnla/"
type: "slovnik"
title: "TNLA – Transport Network Layer Association"
date: 2026-01-01
abbr: "TNLA"
fullName: "Transport Network Layer Association"
category: "Radio Access Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tnla/"
summary: "Logická asociace mezi dvěma síťovými uzly (např. gNB a AMF) přes transportní vrstvu sítě, představující konkrétní transportní cestu nebo koncový bod. Uzel typicky naváže více TNLA pro redundanci a vyr"
---

TNLA je logická asociace mezi dvěma síťovými uzly přes transportní vrstvu sítě, představující konkrétní transportní cestu pro redundanci a vyrovnávání zátěže.

## Popis

Transport Network Layer Association (TNLA) je logický kontext konektivity navázaný mezi dvěma partnerskými síťovými funkcemi přes Transport Network Layer ([TNL](/mobilnisite/slovnik/tnl/)). Představuje konkrétní transportní cestu identifikovanou kombinací adresních informací transportní vrstvy. Například mezi gNB (nebo ng-eNB) a [AMF](/mobilnisite/slovnik/amf/) v systému 5G je TNLA definována pro rozhraní [NG](/mobilnisite/slovnik/ng/) a je asociována s konkrétní asociací protokolu Stream Control Transmission Protocol ([SCTP](/mobilnisite/slovnik/sctp/)). Každá SCTP asociace mezi gNB a AMF, charakterizovaná konkrétní dvojicí IP adres a čísel portů SCTP, tvoří jednu TNLA. Jediné gNB může navázat více TNLA k jedné AMF nebo k více AMF pro redundanci a distribuci zátěže.

Z architektonického hlediska jsou TNLA klíčovou součástí správy rozhraní [N2](/mobilnisite/slovnik/n2/) (NG-C) a N3 (NG-U). Pro řídicí rovinu (N2) každá TNLA podporuje přenos zpráv protokolu NG Application Protocol ([NGAP](/mobilnisite/slovnik/ngap/)). AMF a gNB používají identifikátor TNLA (TNL Association ID) k odkazování na konkrétní transportní cestu při odesílání zpráv. Nastavení TNLA je součástí procedury nastavení rozhraní NG. Koncept se také rozšiřuje na uživatelskou rovinu, kde může být více TNLA použito pro tunely N3 [GTP-U](/mobilnisite/slovnik/gtp-u/) mezi gNB a [UPF](/mobilnisite/slovnik/upf/), ačkoli mechanismy správy se liší.

Jak to funguje, zahrnuje několik procedur. Během počátečního nastavení gNB objeví dostupné AMF a iniciuje navázání SCTP asociací, čímž vytváří TNLA. gNB a AMF si vymění konfigurační data a přiřadí každé asociaci TNL Association ID. Jakmile jsou navázány, zprávy NGAP mohou být odesílány přes jakoukoli dostupnou TNLA k partnerskému uzlu. Koncové body provádějí vyrovnávání zátěže a převzetí služeb při selhání mezi TNLA. Pokud jedna TNLA selže (např. z důvodu selhání cesty nebo SCTP asociace), provoz je plynule přesunut na jinou aktivní TNLA, čímž je zajištěna vysoká dostupnost. Správa TNLA zahrnuje monitorování jejich stavu (up/down), kapacity a výkonu, což je zásadní pro spolehlivost sítě a efektivní distribuci zátěže.

## K čemu slouží

Koncept TNLA byl formálně zaveden a zdůrazněn v 3GPP Release 15 jako součást architektury 5G New Radio (NR) k řešení požadavků na zvýšenou spolehlivost, škálovatelnost a flexibilitu v transportní síti propojující disagregované funkce RAN a core sítě. Jeho vytvoření bylo motivováno potřebou posunu za jednoduché point-to-point linky. Předchozí generace měly redundanční mechanismy, ale servisně orientovaná architektura 5G a cloudové deployment modely vyžadovaly explicitnější a flexibilnější správu transportních cest.

TNLA řeší problém jediného bodu selhání v transportní konektivitě mezi kritickými uzly, jako jsou gNB a AMF. Umožněním více nezávislých transportních cest (TNLA) poskytuje inherentní redundanci. Také řeší vyrovnávání zátěže; síťový provoz (signalizační zátěž) může být distribuován přes více TNLA, aby se předešlo přetížení jediné cesty. To je obzvláště důležité v centralizovaných/cloudových deploymentech RAN, kde se centrální jednotka může připojovat k mnoha distribuovaným jednotkám a core funkcím. Dále TNLA umožňují flexibilní pooling AMF a vyrovnávání zátěže v core síti, protože gNB může mít TNLA k různým AMF v rámci AMF Set. To umožňuje efektivní využití zdrojů a šetrné údržbové operace bez přerušení služby.

## Klíčové vlastnosti

- Představuje logickou transportní cestu, typicky mapovanou na SCTP asociaci pro řídicí rovinu
- Identifikována pomocí TNL Association ID a transportních adres (IP, port)
- Umožňuje více paralelních spojení mezi dvojicí uzlů pro redundanci
- Podporuje vyrovnávání zátěže zpráv aplikačního protokolu (např. NGAP) napříč asociacemi
- Umožňuje nezávislé selhání a obnovu jednotlivých transportních cest
- Základní pro AMF pooling a distribuci workloadu v 5GC

## Související pojmy

- [TNL – Transport Network Layer](/mobilnisite/slovnik/tnl/)
- [SCTP – Stream Control Transmission Protocol](/mobilnisite/slovnik/sctp/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 37.483** (Rel-19) — E1 Application Protocol (E1AP)
- **TS 38.413** (Rel-19) — NG Application Protocol (NGAP)
- **TS 38.463** (Rel-19) — E1 Application Protocol (E1AP)

---

📖 **Anglický originál a plná specifikace:** [TNLA na 3GPP Explorer](https://3gpp-explorer.com/glossary/tnla/)
