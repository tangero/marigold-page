---
slug: "nasdvm"
url: "/mobilnisite/slovnik/nasdvm/"
type: "slovnik"
title: "NASDVM – Non-Access Stratum Data via MME"
date: 2025-01-01
abbr: "NASDVM"
fullName: "Non-Access Stratum Data via MME"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/nasdvm/"
summary: "NASDVM je bezpečnostní mechanismus, který umožňuje MME bezpečně přenášet malá množství dat mezi uživatelským zařízením (UE) a aplikačním serverem pomocí signalizace NAS. Využívá stávající bezpečnostní"
---

NASDVM je bezpečnostní mechanismus pro přenos malého množství dat mezi uživatelským zařízením (UE) a aplikačním serverem prostřednictvím signalizace NAS, který pro zajištění integrity a důvěrnosti využívá stávající bezpečnostní kontext NAS bez nutnosti plnohodnotného přenosového kanálu (beareru) v uživatelské rovině.

## Popis

Non-Access Stratum Data via [MME](/mobilnisite/slovnik/mme/) (NASDVM) je funkce definovaná v 3GPP, primárně v bezpečnostní specifikaci TS 33.401. Jedná se o metodu pro přenos omezeného množství dat aplikační vrstvy mezi uživatelským zařízením (UE) a síťovým aplikačním serverem zapouzdřením těchto dat do stávajících signalizačních zpráv Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)). Klíčovou entitou, která tento přenos zprostředkovává, je Mobility Management Entity (MME) v Evolved Packet Core (EPC). Namísto vytváření tradičního připojení k paketové síti (PDN) s vyhrazeným přenosovým kanálem a prostředky uživatelské roviny jsou data přenášena navázaná na signalizaci řídicí roviny, konkrétně uvnitř zpráv NAS Transport. To je vysoce efektivní pro občasný přenos malých dat, typický pro mnoho aplikací internetu věcí (IoT) a komunikace mezi stroji ([MTC](/mobilnisite/slovnik/mtc/)).

Provozní postup zahrnuje využití bezpečnostního kontextu EPS NAS, který je již navázán během procedury připojení (attach) prostřednictvím EPS [AKA](/mobilnisite/slovnik/aka/), uživatelským zařízením (UE) a MME. Když aplikace na UE potřebuje odeslat data, předá je vrstvě NAS. Vrstva NAS tato data zapouzdří do zprávy NAS (např. zprávy Uplink NAS Transport). Celá tato zpráva NAS, včetně zapouzdřených aplikačních dat, je pak chráněna na integritu a zašifrována pomocí bezpečnostních klíčů NAS (KNASint, KNASenc), stejně jako jakákoli jiná signalizační zpráva NAS. Zpráva je odeslána přes Access Stratum ([RRC](/mobilnisite/slovnik/rrc/) přes LTE) k [eNB](/mobilnisite/slovnik/enb/), který ji přepošle k MME přes rozhraní S1-AP. MME po ověření integrity a dešifrování zprávy extrahuje aplikační data.

MME poté funguje jako přenosový člen nebo brána k aplikačnímu serveru. Musí určit cíl pro tato aplikační data. To je typicky konfigurováno na základě předplatného UE nebo konkrétní služební žádosti. MME přepošle extrahovaná datová užitečná data příslušnému aplikačnímu serveru ([AS](/mobilnisite/slovnik/as/)) přes zabezpečené rozhraní, například pomocí protokolů založených na Diameter nebo Service Capability Exposure Function (SCEF). Zpětná cesta funguje podobně: AS odešle data k MME, která je zapouzdří do zprávy Downlink NAS Transport, zabezpečí je pomocí bezpečnostního kontextu NAS pro dané UE a doručí je přes rozhraní S1 a RRC. Celý tento proces probíhá bez aktivace přenosového kanálu v uživatelské rovině pro UE, což umožňuje udržet UE po delší dobu v energeticky úsporném stavu idle.

NASDVM je klíčovým prvkem optimalizace Control Plane CIoT EPS, souboru funkcí navržených pro zařízení IoT. Její integrace s vrstvou NAS poskytuje inherentní bezpečnostní výhody. Data mají prospěch ze stejné silné, koncové (UE-to-MME) kryptografické ochrany jako kritická signalizace správy mobility. To odstraňuje potřebu, aby aplikace pro tato malá data implementovala vlastní zabezpečení na transportní vrstvě (jako TLS), čímž šetří výpočetní výkon a signalizační režii na zařízení s omezenými prostředky. Je však navržena pro občasné přenosy malých datových paketů, protože časté použití by negovalo výhody úspory energie a přetížilo signalizační síť řídicí roviny.

## K čemu slouží

NASDVM byla vytvořena, aby vyřešila základní výzvu při připojování obrovského množství levných, nízkopříkonových zařízení IoT k celulárním sítím: signalizační a energetickou režii spojenou se zřizováním tradičních datových připojení. Před optimalizacemi jako je NASDVM muselo IoT zařízení potřebující odeslat několik bajtů dat (např. teplotní údaj) provést úplnou proceduru služební žádosti. To zahrnuje přechod ze stavu idle do stavu connected, zřízení alespoň jednoho datového rádiového kanálu a kanálu S1-U a provedení veškeré související signalizace [RRC](/mobilnisite/slovnik/rrc/) a S1-AP. Po odeslání dat by se připojení zrušilo. Tento proces spotřebovává významnou část energie baterie na zařízení a vytváří značné signalizační zatížení sítě pro minimální množství přenášených dat.

Motivace pro NASDVM vycházela z práce 3GPP na komunikaci mezi stroji (MTC) a Cellular IoT (CIoT) začínající ve verzi 12 a plně specifikované ve verzi 13. Cílem bylo definovat síťové optimalizace, které by mohly efektivně podporovat miliony takových zařízení. NASDVM jako součást optimalizace Control Plane CIoT EPS to řeší přizpůsobením vždy nezbytné signalizační cesty NAS. Protože se zařízení musí k síti připojit (attach) a udržovat bezpečnostní kontext NAS pro správu mobility, je tento stávající zabezpečený kanál využit k přenosu aplikačních dat. Tím odpadá potřeba samostatného, na zdroje náročného nastavení uživatelské roviny.

Tento přístup přímo řeší omezení předchozích architektur pro občasný přenos dat. Snižuje spotřebu energie zařízení minimalizací doby, po kterou musí být rádiový modul zařízení aktivní ve stavu connected s vysokým příkonem. Snižuje latenci pro přenos malých dat, protože data mohou být odeslána okamžitě v rámci stávající signalizační procedury. Dále zmírňuje signalizační přetížení na rozhraních RAN a jádra sítě tím, že se vyhne zřizování a rušení přenosových kanálů pro každý malý datový paket. V podstatě byla NASDVM vytvořena, aby učinila celulární sítě životaschopnými a efektivními pro novou třídu zařízení s omezenými prostředky, což umožňuje realizaci vize IoT ve velkém měřítku bez nutnosti přestavby základních bezpečnostních a mobilních principů LTE.

## Klíčové vlastnosti

- Přenáší aplikační data uvnitř signalizačních zpráv NAS chráněných na integritu a zašifrovaných
- Odstraňuje potřebu zřizování přenosového kanálu v uživatelské rovině pro přenos malých dat
- Využívá stávající bezpečnostní kontext EPS NAS (KNASint, KNASenc) pro ochranu
- Umožňuje efektivní komunikaci pro energeticky omezená zařízení IoT/Cellular IoT
- Implementována jako součást optimalizace Control Plane CIoT EPS
- MME funguje jako zabezpečený přenosový člen mezi UE a aplikačním serverem

## Definující specifikace

- **TS 33.401** (Rel-19) — EPS Security Architecture

---

📖 **Anglický originál a plná specifikace:** [NASDVM na 3GPP Explorer](https://3gpp-explorer.com/glossary/nasdvm/)
