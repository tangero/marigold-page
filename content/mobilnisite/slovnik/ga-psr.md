---
slug: "ga-psr"
url: "/mobilnisite/slovnik/ga-psr/"
type: "slovnik"
title: "GA-PSR – Generic Access - Packet Switched Resources"
date: 2025-01-01
abbr: "GA-PSR"
fullName: "Generic Access - Packet Switched Resources"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ga-psr/"
summary: "Komponenta sítě Generic Access Network (GAN), která umožňuje mobilnímu zařízení přístup k paketovým datovým službám GPRS/UMTS přes nelicencovanou bezdrátovou IP síť (např. Wi-Fi). Integruje Wi-Fi dato"
---

GA-PSR je komponenta sítě Generic Access Network, která umožňuje mobilním zařízením přístup k paketovým službám GPRS/UMTS přes nelicencovanou bezdrátovou IP síť (např. Wi-Fi), a integruje je s mobilním jádrem.

## Popis

Generic Access - Packet Switched Resources (GA-PSR) je protějškem [GA-CSR](/mobilnisite/slovnik/ga-csr/) v rámci architektury 3GPP Generic Access Network ([GAN](/mobilnisite/slovnik/gan/)) a je odpovědný za poskytování paketových datových služeb. Umožňuje uživatelskému zařízení (UE) navázat datovou relaci a přistupovat ke službám, jako je prohlížení internetu, e-mail a IMS, přes zabezpečené IP spojení prostřednictvím nelicencované rádiové technologie (např. Wi-Fi), přičemž je plně spravován jádrovou sítí mobilního operátora.

Funkčně GA-PSR spolupracuje s GA-CSR na straně UE a s Generic Access Network Controllerem ([GANC](/mobilnisite/slovnik/ganc/)). Vrstva [GA](/mobilnisite/slovnik/ga/) v UE zapouzdří veškerou signalizaci [GPRS](/mobilnisite/slovnik/gprs/) ([GMM/SM](/mobilnisite/slovnik/gmm-sm/)) a pakety uživatelských dat do paketů zabezpečených [IPsec](/mobilnisite/slovnik/ipsec/) pro přenos přes širokopásmové IP spojení. Na straně GANC funkce GA-PSR tento zabezpečený tunel ukončuje. Následně předává signalizaci GPRS do Serving GPRS Support Node (SGSN) přes standardní rozhraní Gb nebo Iu-ps. V uživatelské rovině funkce GA-PSR přeposílá datové pakety mezi IPsec tunelem UE a [GTP-U](/mobilnisite/slovnik/gtp-u/) tunelem, který je zřízen mezi GANC (fungujícím jako proxy BSS/NodeB) a SGSN/GGSN.

Tato architektura zajišťuje, že všechny kontexty paketových datových protokolů (PDP) jsou centrálně spravovány SGSN. Operátor si zachovává kontrolu nad autentizací (prostřednictvím SIM přihlašovacích údajů), účtováním a vynucováním politik (např. filtrování APN) i pro provoz procházející přes Wi-Fi. GA-PSR podporuje procedury mobility, umožňuje pozastavení datové relace na Wi-Fi a její obnovení v mobilní síti, nebo v některých implementacích i její hladký přenos. Poskytuje jednotný zážitek z datových služeb, který překlenuje propast mezi mobilními daty a nedůvěryhodným přístupem přes WLAN.

## K čemu slouží

GA-PSR byl vyvinut, aby rozšířil výhody GAN/UMA i na paketové datové služby. Zatímco I-WLAN poskytovala metodu pro datový přístup přes Wi-Fi, často vyžadovala samostatný tok pro autentizaci a účtování. GA-PSR usiloval o hlubší integraci, která umožňuje operátorům nabízet plně bezproblémovou datovou službu, kde byl přístupový síťový prostředek (mobilní síť nebo Wi-Fi) abstrahován od uživatele a od servisní platformy.

Řešil problém roztříštěného uživatelského zážitku a složitého účtování pro uživatele dvoupásmových zařízení. Bez GA-PSR mohlo použití Wi-Fi pro data znamenat spuštění samostatného spojovacího manažera, ztrátu přístupu k operátorským službám nebo samostatné účtování. GA-PSR umožnil operátorovi zacházet s Wi-Fi přístupem jako s další rádiovou přístupovou technologií pod jeho přímou kontrolou, což umožnilo konzistentní servisní politiky, jednotné záznamy o účtování a přístup k službám specifickým pro účastníka, jako jsou portály operátora nebo IMS.

Vytvoření GA-PSR bylo motivováno snahou o skutečnou konvergenci pevných a mobilních sítí (FMC) pro všechny služby. Umožnilo mobilním operátorům využít hustá nasazení Wi-Fi k odlehčení datového provozu z přetížených makro buněk mobilní sítě, při zachování přehledu a kontroly nad datovou relací účastníka. Jednalo se o strategický nástroj pro konkurenci s čistými poskytovateli internetových služeb a pro nákladově efektivní zvládání explozivního růstu poptávky po mobilních datech.

## Klíčové vlastnosti

- Umožňuje paketové datové služby GPRS/UMTS přes nelicencované IP přístupové sítě
- Integruje datové relace přes Wi-Fi do paketové sítě jádra operátora (SGSN/GGSN)
- Používá IPsec pro zabezpečené tunelování veškeré signalizace GPRS a dat uživatelské roviny
- Podporuje standardní procedury aktivace, modifikace a deaktivace kontextů PDP
- Umožňuje autentizaci, účtování a vynucování politik pod kontrolou operátora
- Usnadňuje mechanismy kontinuity datové relace mezi Wi-Fi a mobilním přístupem

## Související pojmy

- [GA-CSR – Generic Access - Circuit Switched Resources](/mobilnisite/slovnik/ga-csr/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [IPSec – Internet Protocol Security](/mobilnisite/slovnik/ipsec/)

## Definující specifikace

- **TS 43.318** (Rel-19) — Generic Access Network (GAN) Stage 2
- **TR 43.902** (Rel-19) — GAN Enhancements Feasibility Study
- **TS 44.318** (Rel-19) — Generic Access Network (GAN) Interface Procedures

---

📖 **Anglický originál a plná specifikace:** [GA-PSR na 3GPP Explorer](https://3gpp-explorer.com/glossary/ga-psr/)
