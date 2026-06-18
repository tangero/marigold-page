---
slug: "ensi"
url: "/mobilnisite/slovnik/ensi/"
type: "slovnik"
title: "ENSI – External Network Slice Information"
date: 2026-01-01
abbr: "ENSI"
fullName: "External Network Slice Information"
category: "Network Slicing"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/ensi/"
summary: "ENSI je parametr sloužící k identifikaci a výběru konkrétní instance síťového segmentu pro koncové zařízení (UE) při roamingu nebo při připojení k externí síti. Umožňuje domovské síti poskytnout navšt"
---

ENSI je parametr, který identifikuje konkrétní instanci síťového segmentu pro koncové zařízení (UE) v roamingu a umožňuje domovské síti předat informace pro výběr segmentu navštívené síti.

## Popis

External Network Slice Information (ENSI, informace o externím síťovém segmentu) je klíčová komponenta rámce síťového segmentování 3GPP, a to zejména pro scénáře roamingu. Je definována jako řetězec jednoznačně identifikující instanci síťového segmentu. Když se koncové zařízení (UE) přihlásí do navštívené veřejné pozemní mobilní sítě ([VPLMN](/mobilnisite/slovnik/vplmn/)), může domovská síť ([HPLMN](/mobilnisite/slovnik/hplmn/)) uvést ENSI v rámci předplatitelských dat nebo během registrační procedury, aby označila, kterou konkrétní instanci segmentu je UE oprávněno používat. VPLMN tuto informaci použije spolu s dalšími parametry, jako je Subscribed Network Slice Selection Assistance Information ([S-NSSAI](/mobilnisite/slovnik/s-nssai/)), k namapování požadavku na lokálně dostupnou a ekvivalentní instanci síťového segmentu ([NSI](/mobilnisite/slovnik/nsi/)). ENSI je přenášeno v signalizačních zprávách ne-přístupové vrstvy ([NAS](/mobilnisite/slovnik/nas/)), například v registračním požadavku, a je zpracováváno funkcí správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) jak v domovské, tak v navštívené síti.

Z architektonického hlediska funguje ENSI v rámci funkce pro výběr síťového segmentu ([NSSF](/mobilnisite/slovnik/nssf/)) a AMF. Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) domovské sítě HPLMN uchovává ENSI jako součást kontextu předplatitele. Během počáteční registrace nebo procedur služebního požadavku, pokud je UE v roamingu, může AMF nebo NSSF domovské sítě HPLMN určit příslušné ENSI a zahrnout jej do odpovědi směrem k VPLMN. AMF navštívené sítě VPLMN po přijetí ENSI spolupracuje se svým lokálním NSSF. NSSF provede mapování přijaté dvojice S-NSSAI a ENSI na NSI specifické pro VPLMN. Toto mapování je klíčové, protože identifikátory segmentů (S-NSSAI) jsou jedinečné pouze v rámci jedné PLMN; ENSI poskytuje dodatečnou úroveň podrobnosti potřebnou pro to, aby VPLMN mohla vybrat přesně tu instanci segmentu, kterou zamýšlel domovský operátor.

Úlohou ENSI je překlenout sémantickou mezeru mezi identifikátory síťových segmentů v různých správních doménách. Bez ENSI by VPLMN mohla obdržet pouze S-NSSAI, které popisuje typ segmentu (např. Enhanced Mobile Broadband, Massive IoT), nikoli však konkrétní instanci. V HPLMN může existovat více instancí stejného typu segmentu (např. různé eMBB segmenty pro různé podnikové zákazníky). ENSI umožňuje HPLMN přesně určit konkrétní instanci, což VPLMN umožňuje poskytnout uživatelskou zkušenost odpovídající politikám segmentace domovské sítě, včetně konkrétních charakteristik kvality služby (QoS), bezpečnostních politik a konfigurací síťových funkcí. Jde o klíčový prvek pro pokročilé roamingové dohody zahrnující síťové segmentování, který zajišťuje konzistenci segmentu na end-to-end bázi a plnění smluv o úrovni služeb (SLA) přes hranice operátorů.

## K čemu slouží

ENSI bylo zavedeno, aby vyřešilo problém výběru a identifikace síťového segmentu v mezisfénových (roamingových) scénářích. Protože sítě 5G začaly využívat síťové segmentování k nabídnutí přizpůsobených logických sítí pro různé služby, bylo zapotřebí mechanismu pro rozšíření těchto schopností na uživatele mimo jejich domovskou síť. Před zavedením ENSI byl výběr segmentu primárně založen na S-NSSAI, které je jedinečné pouze v rámci sítě jednoho operátora. Při roamingu by navštívená síť přijímající pouze S-NSSAI nevěděla, kterou konkrétní instanci tohoto typu segmentu má přiřadit, což by mohlo vést k nesprávnému mapování služeb nebo neschopnosti dodržet podrobné SLA specifická pro segment.

Vytvoření ENSI bylo motivováno komerční potřebou globální kontinuity služeb pro podnikové a vertikální aplikace využívající síťové segmenty. Například nadnárodní společnost využívající vyhrazený URLLC segment pro automatizaci továrny by vyžadovala, aby charakteristiky tohoto segmentu zůstaly zachovány, když se zařízení zaměstnance připojí v roamingu k síti partnerského operátora. ENSI poskytuje technický parametr, který domovské síti umožňuje sdělit: "Použij *tuto konkrétní* instanci URLLC segmentu", což navštívené síti umožní tento požadavek splnit, pokud je pod roamingovou dohodou dostupný kompatibilní segment. Řeší tak omezení předchozích přístupů, kdy povědomí o segmentech bylo omezeno na jedinou síť, a odemyká tím plný ekonomický a technický potenciál síťového segmentování 5G v globálním ekosystému.

## Klíčové vlastnosti

- Jednoznačně identifikuje konkrétní instanci síťového segmentu (NSI) v rámci domovské PLMN
- Umožňuje přesný výběr segmentu pro koncová zařízení (UE) v roamingu napříč různými síťami operátorů
- Přenášeno v signalizačních zprávách ne-přístupové vrstvy (NAS) (např. registrační požadavek) pro správu mobility s ohledem na segmenty
- Používáno funkcí NSSF navštívené sítě k mapování záměru domovské sítě ohledně segmentu na lokální NSI
- Podporuje plnění end-to-end smluv o úrovni služeb (SLA) pro služby využívající segmenty během roamingu
- Nezbytné pro pokročilé roamingové dohody zahrnující garantovaný výkon a izolaci segmentů

## Definující specifikace

- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures

---

📖 **Anglický originál a plná specifikace:** [ENSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ensi/)
