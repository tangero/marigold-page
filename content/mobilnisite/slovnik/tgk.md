---
slug: "tgk"
url: "/mobilnisite/slovnik/tgk/"
type: "slovnik"
title: "TGK – Traffic Generating Key"
date: 2026-01-01
abbr: "TGK"
fullName: "Traffic Generating Key"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tgk/"
summary: "Kryptografický klíč používaný v sítích 3GPP pro generování bezpečných, realistických vzorců provozu pro systémy zákonného odposlechu a monitorování. Zajišťuje, že odposlechnutý provoz je nerozlišiteln"
---

TGK je kryptografický klíč používaný v sítích 3GPP pro generování bezpečného, realistického provozu pro systémy zákonného odposlechu, který zajišťuje, že odposlechnutá data jsou nerozlišitelná od skutečného uživatelského provozu.

## Popis

Traffic Generating Key (TGK) je bezpečnostní parametr definovaný v architektuře zákonného odposlechu ([LI](/mobilnisite/slovnik/li/)) a zabezpečení 3GPP. Jedná se o kryptografický klíč, typicky odvozený z hierarchie klíčů zahrnující jiné dlouhodobé nebo relací klíče, který je používán konkrétně síťovými funkcemi zodpovědnými za generování fiktivního nebo doplňkového provozu. Tento doplňkový provoz je vkládán do odposlechnutých komunikačních toků, když skutečný objem uživatelského provozu není dostatečný pro splnění regulatorních požadavků na kontinuální tok dat. Primární technická role TGK spočívá v inicializaci funkce pseudo-náhodného generování provozu. Tato funkce vytváří datové vzorce napodobující statistické vlastnosti, velikosti paketů a časování reálného uživatelského nebo signalizačního provozu, čímž zabraňuje externímu pozorovateli nebo odposlechnuté straně detekovat přítomnost odposlechu na základě anomálních mezer nebo vzorců v datovém toku.

Z architektonického hlediska je TGK spravován a poskytován bezpečnostními řídicími funkcemi, často ve spolupráci s funkcí zákonného odposlechu ([LIF](/mobilnisite/slovnik/lif/)) nebo mediační funkcí ([MF](/mobilnisite/slovnik/mf/)), jak je specifikováno v TS 33.108 a souvisejících dokumentech. Je bezpečně doručen k síťovému uzlu provádějícímu odposlech a generování provozu, jako je Gateway [GPRS](/mobilnisite/slovnik/gprs/) Support Node (GGSN), Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) nebo specializovaný odposlechový gateway. Životní cyklus klíče – generování, distribuce, aktivace a odstranění – je přísně kontrolován a logován, aby byla zajištěna nepopiratelnost a soulad s právními rámci.

Během provozu, když je pro cíl aktivován zákonný odposlech a skutečný tok provozu klesne pod stanovený práh, odposlechový uzel použije TGK ke generování doplňkového provozu. Generovací algoritmus zajišťuje, že výstup je kryptograficky bezpečný a bez znalosti klíče nepředvídatelný, díky čemuž je doplňkový provoz nerozlišitelný od šifrovaného reálného provozu. Tento proces je klíčový pro zachování požadovaného formátu odposlechnutých komunikací, jako jsou standardy rozhraní Handover Interface ([HI](/mobilnisite/slovnik/hi/)), a pro zabránění cíli použít analýzu provozu k odvození, že je pod dohledem. TGK tedy funguje na průsečíku kryptografické bezpečnosti, síťových operací a regulatorní shody a umožňuje efektivní a utajený zákonný odposlech.

## K čemu slouží

TGK byl zaveden k řešení konkrétní technické výzvy v systémech zákonného odposlechu: požadavku na kontinuální, nepřerušovaný tok odposlechnutých dat, a to i když cíl aktivně nekomunikuje. Rané odposlechové systémy, které pouze přeposílaly uživatelský provoz, vytvářely nepravidelné datové záplaty, což mohlo prozradit místo nebo aktivitu odposlechu. Regulační standardy často vyžadují konstantní tok dat do určitých monitorovacích zařízení odposlechu za účelem zjednodušení zpracování a ukládání dat. TGK tento problém řeší tím, že umožňuje síti generovat realistická, bezpečná doplňková data.

Jeho vytvoření bylo motivováno potřebou zvýšeného utajení a integrity v odposlechových operacích. Bez bezpečné metody by generovaný doplňkový provoz mohl být statisticky identifikovatelný nebo dokonce padělatelný, což by ohrozilo vyšetřování. TGK poskytuje kryptografický základ, který zajišťuje, že doplňková data jsou stejně bezpečná a neprůhledná jako šifrovaný provoz skutečného uživatele. To je v souladu s širším cílem 3GPP standardizovat rozhraní zákonného odposlechu ([LI](/mobilnisite/slovnik/li/)) za účelem zajištění interoperability, spolehlivosti a právní shody napříč různými síťovými dodavateli a operátory.

Historicky, jak se sítě vyvíjely směrem k plně IP architekturám s různorodými a přerušovanými vzorci provozu, potřeba takového standardizovaného, bezpečného mechanismu generování provozu se stala kritickou. TGK, zavedený ve verzi 9 jako součást probíhajících vylepšení LI, formalizoval metodu, která byla jak technicky robustní, tak právně obhajitelná, a řešila tak omezení ad-hoc nebo nekryptografických doplňkových řešení používaných v dřívějších generacích sítí.

## Klíčové vlastnosti

- Kryptografické generování pseudo-náhodného doplňkového provozu
- Zajišťuje kontinuitu toku provozu pro rozhraní zákonného odposlechu
- Uchovává utajení odposlechu napodobováním vzorců reálného provozu
- Integrován do hierarchií klíčů zabezpečení a zákonného odposlechu 3GPP
- Spravován bezpečnými funkcemi poskytování a správy životního cyklu
- Zabraňuje detekci pomocí analýzy provozu nebo rozpoznávání vzorců

## Definující specifikace

- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 29.828** (Rel-12) — IMS Media Plane Security H.248 Profiles Study
- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service
- **TS 33.328** (Rel-19) — IMS Media Plane Security Specification

---

📖 **Anglický originál a plná specifikace:** [TGK na 3GPP Explorer](https://3gpp-explorer.com/glossary/tgk/)
