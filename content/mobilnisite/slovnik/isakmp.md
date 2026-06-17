---
slug: "isakmp"
url: "/mobilnisite/slovnik/isakmp/"
type: "slovnik"
title: "ISAKMP – Internet Security Association Key Management Protocol"
date: 2025-01-01
abbr: "ISAKMP"
fullName: "Internet Security Association Key Management Protocol"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/isakmp/"
summary: "ISAKMP je rámec pro navazování bezpečnostních asociací (SA) a kryptografických klíčů v tunelech založených na IPsec. V 3GPP se používá ve specifikaci NDS/IP (Network Domain Security for IP) pro zabezp"
---

ISAKMP je rámec pro navazování bezpečnostních asociací (SA) a kryptografických klíčů, používaný ve specifikaci NDS/IP konsorcia 3GPP pro zabezpečení komunikace mezi síťovými entitami, jako jsou eNB a jádro sítě.

## Popis

Internet Security Association Key Management Protocol (ISAKMP) je protokolový rámec definovaný [IETF](/mobilnisite/slovnik/ietf/) (RFC 2408) pro navazování, vyjednávání, modifikaci a rušení bezpečnostních asociací (SA) a odpovídajících kryptografických klíčů. Bezpečnostní asociace (SA) je jednosměrné spojení, které poskytuje přenášenému provozu bezpečnostní služby. ISAKMP definuje postupy a formáty paketů pro autentizaci, navázání klíčů a správu klíčů. Je nezávislý na konkrétním protokolu pro výměnu klíčů, autentizační metodě nebo šifrovacím algoritmu, což z něj činí flexibilní rámec. V 3GPP je ISAKMP povinnou součástí specifikace Network Domain Security for IP ([NDS/IP](/mobilnisite/slovnik/nds-ip/)) (TS 33.210) pro zabezpečení IP komunikace na řídicí a uživatelské rovině mezi síťovými prvky, zejména v rádiové přístupové síti (RAN) a mezi RAN a prvky jádra sítě. Například se používá pro zabezpečení rozhraní S1 mezi eNodeB ([eNB](/mobilnisite/slovnik/enb/)) a Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/))/Serving Gateway (S-GW) a rozhraní X2 mezi eNB v LTE sítích, a obdobně pro rozhraní NG-RAN v 5G. Protokol funguje ve dvou fázích: Fáze 1 naváže zabezpečený, autentizovaný kanál (ISAKMP SA) mezi dvěma protistranami, který je pak použit k ochraně vyjednávání ve Fázi 2. Fáze 2 navazuje SA pro jiné protokoly, jako je [IPsec](/mobilnisite/slovnik/ipsec/) [ESP](/mobilnisite/slovnik/esp/) nebo [AH](/mobilnisite/slovnik/ah/), které budou použity k zabezpečení skutečného uživatelského nebo řídicího provozu. Pakety ISAKMP používají UDP port 500. V rámci NDS/IP se ISAKMP typicky používá s IKEv1 nebo IKEv2 jako protokolem pro výměnu klíčů k provedení vzájemné autentizace (často pomocí předem sdílených klíčů nebo certifikátů) a k odvození klíčů pro IPsec SA.

## K čemu slouží

ISAKMP byl vytvořen, aby poskytl standardizovaný, škálovatelný a bezpečný rámec pro správu bezpečnostních asociací v IP sítích, což je základním požadavkem pro budování důvěryhodných VPN a zabezpečení komunikace mezi uzly. V rámci 3GPP bylo přijetí ISAKMP jako součásti [NDS/IP](/mobilnisite/slovnik/nds-ip/) motivováno přechodem na plně IP síťové architektury ve verzi 3GPP Release 5 a novějších. Jak se síťová rozhraní přesunula ze starších, často fyzicky chráněných TDM/ATM spojů na paketově přepínané IP sítě, stala se zranitelnými vůči odposlechu, falšování a dalším útokům na IP vrstvě. Účelem NDS/IP, a tedy i ISAKMP, je poskytnout zabezpečení na IP vrstvě mezi důvěryhodnými síťovými prvky 3GPP po jednotlivých skocích (hop-by-hop), což zajišťuje důvěrnost, integritu a autentizaci signalizačních a uživatelských dat přenášených přes tato rozhraní. Tím se řeší bezpečnostní mezera vytvořená přechodem na čistě IP. Před zavedením NDS/IP byla často za dostačující považována fyzická ochrana spojů. ISAKMP poskytuje flexibilní, standardy založenou metodu pro automatizaci navazování a správy životního cyklu IPsec tunelů, které tyto kritické síťové spoje chrání, čímž snižuje potřebu ruční konfigurace a umožňuje dynamickou autentizaci protistran a obnovu klíčů.

## Klíčové vlastnosti

- Rámec pro navazování, vyjednávání, modifikaci a rušení bezpečnostních asociací (SA)
- Provozní nezávislost na konkrétních protokolech pro výměnu klíčů, šifrování nebo autentizačních algoritmech
- Dvoufázový provoz: Fáze 1 pro navázání zabezpečeného řídicího kanálu (ISAKMP SA), Fáze 2 pro navázání SA specifických pro daný protokol (např. pro IPsec)
- Podpora více autentizačních metod (předem sdílené klíče, digitální podpisy, šifrování veřejným klíčem)
- Definuje datové jednotky (payloads) a výměny pro atributy SA, návrhy a oznámení
- Pro přenos používá UDP port 500, což poskytuje mechanismy spojení nevyžadující navázání spojení (connectionless), ale spolehlivé

## Související pojmy

- [NDS/IP – Network Domain Security for IP based Protocols](/mobilnisite/slovnik/nds-ip/)
- [IPSec – Internet Protocol Security](/mobilnisite/slovnik/ipsec/)
- [IKE – Internet Key Exchange](/mobilnisite/slovnik/ike/)

## Definující specifikace

- **TS 33.210** (Rel-19) — UMTS Security for IP Networks

---

📖 **Anglický originál a plná specifikace:** [ISAKMP na 3GPP Explorer](https://3gpp-explorer.com/glossary/isakmp/)
