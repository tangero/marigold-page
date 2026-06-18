---
slug: "csk-id"
url: "/mobilnisite/slovnik/csk-id/"
type: "slovnik"
title: "CSK-ID – Client-Server Key Identifier"
date: 2026-01-01
abbr: "CSK-ID"
fullName: "Client-Server Key Identifier"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/csk-id/"
summary: "Kryptografický identifikátor používaný v architektuře GBA (Generic Bootstrapping Architecture) konsorcia 3GPP k jednoznačné referenci sdíleného tajného klíče navázaného mezi klientem (UE) a síťovou ap"
---

CSK-ID je kryptografický identifikátor používaný v architektuře GBA (Generic Bootstrapping Architecture) konsorcia 3GPP k jednoznačné referenci sdíleného tajného klíče mezi klientem a síťovou aplikační funkcí, což umožňuje zabezpečené ověřování pro služby aplikační vrstvy.

## Popis

Identifikátor klient-server klíče (CSK-ID) je základní komponentou v rámci architektury [GBA](/mobilnisite/slovnik/gba/) (Generic Bootstrapping Architecture) konsorcia 3GPP, což je rámec využívající bezpečnostní přihlašovací údaje univerzálního identifikačního modulu účastníka ([USIM](/mobilnisite/slovnik/usim/)) k navázání aplikačně specifických bezpečnostních asociací. Funguje jako jedinečná reference nebo ukazatel na konkrétní sdílený tajný klíč, známý jako klíč Ks (Bootstrapping Session Key), který je odvozen během procedury GBA bootstrapping mezi uživatelským zařízením (UE) a funkcí bootstrapovacího serveru ([BSF](/mobilnisite/slovnik/bsf/)). CSK-ID není samotný klíč, ale kryptograficky generovaný identifikátor, který umožňuje jak UE, tak síťové aplikační funkci ([NAF](/mobilnisite/slovnik/naf/)) jednoznačně identifikovat a odkazovat se na konkrétní instanci klíče Ks a s ní spojený kontext relace pro následné ověřování a dohodu o klíči.

Generování a životní cyklus CSK-ID jsou úzce spojeny s procedurou GBA bootstrapping. Když UE iniciuje bootstrapování, ověří se u BSF pomocí svých přihlašovacích údajů USIM (prostřednictvím protokolu [AKA](/mobilnisite/slovnik/aka/) – Authentication and Key Agreement). Po úspěšném ověření BSF a UE nezávisle odvodí hlavní relakční klíč Ks. BSF následně vygeneruje identifikátor bootstrapovací transakce ([B-TID](/mobilnisite/slovnik/b-tid/)) a odpovídající CSK-ID. B-TID je odeslán k UE a slouží jako primární identifikátor relace. CSK-ID je však specificky určen pro použití mezi UE a NAF. Je odvozen z B-TID a dalších parametrů, což zajišťuje kryptograficky bezpečné propojení s klíčem Ks. BSF ukládá klíč Ks, B-TID a CSK-ID spolu s identitou účastníka a dobou platnosti klíče.

Když UE později potřebuje přistoupit ke službě poskytované konkrétní NAF (např. službě multimediální telefonie nebo IoT platformě), odešle této NAF CSK-ID jako součást žádosti o službu. NAF, která nemá s UE přímou bezpečnostní asociaci, přepošle tento CSK-ID k BSF k ověření. BSF použije CSK-ID k vyhledání odpovídajícího klíče Ks a profilu účastníka. Poté vygeneruje pro NAF specifický klíč Ks_NAF, odvozený z Ks a jedinečného identifikátoru NAF, a poskytne tento Ks_NAF (nebo token z něj odvozený) zpět NAF. UE nezávisle odvodí stejný klíč Ks_NAF. Tím se mezi UE a NAF naváže sdílené tajemství, které umožňuje vzájemné ověření a zabezpečenou komunikaci pro danou aplikační relaci, a to vše bez nutnosti, aby NAF musela zpracovávat dlouhodobé přihlašovací údaje USIM uživatele.

Architektura zahrnuje několik klíčových síťových funkcí: UE (klient), BSF (která provádí bootstrapování), server domovského účastníka ([HSS](/mobilnisite/slovnik/hss/)), který poskytuje autentizační vektory, a NAF (aplikační server). CSK-ID funguje jako kritický referenční token, který tyto entity bezpečně propojuje. Jeho návrh zajišťuje, že různé NAF obdrží různé odvozené klíče (Ks_NAF), i když odkazují na stejný základní klíč Ks prostřednictvím stejného CSK-ID, čímž poskytuje izolaci služeb. Formát a zpracování tohoto identifikátoru jsou standardizovány v dokumentech 3GPP TS 24.380 (GBA Push) a TS 33.220 (GBA), což zajišťuje interoperabilitu napříč dodavateli a síťovými nasazeními.

## K čemu slouží

CSK-ID byl vytvořen, aby řešil výzvu poskytování bezpečného a škálovatelného ověřování pro mnohočetné IP-based aplikační služby v mobilních sítích, aniž by zatěžoval každou službu správou vlastních uživatelských přihlašovacích údajů nebo autentizační infrastruktury. Před zavedením [GBA](/mobilnisite/slovnik/gba/) často aplikační služby vyžadovaly samostatné přihlašovací údaje typu uživatelské jméno/heslo nebo složitou správu certifikátů, což zhoršovalo uživatelský zážitek a zvyšovalo provozní režii. Jádrem problému bylo, jak využít silné ověřování založené na SIM kartě, již přítomné v celulárních sítích, pro zabezpečení přidaných služeb.

GBA a CSK-ID to řeší tím, že umožňují jedinou, sítí asistovanou bootstrapovací událost generovat bezpečné klíče pro více aplikačních serverů. CSK-ID poskytuje nezbytný mechanismus pro aplikační server (NAF), aby se dotázal centrální bezpečnostní autority sítě (BSF) a získal službě specifický klíč odvozený z primárních přihlašovacích údajů uživatele. Tím odděluje aplikační zabezpečení od ověřování v jádru sítě, což umožňuje poskytovatelům služeb nabízet zabezpečené služby bez přímého přístupu k citlivým datům účastníka. Usnadňuje koncept 'single sign-on' pro mobilní aplikace, kde lze síťové ověření bezpečně znovu použít napříč různorodými službami.

Vytvoření CSK-ID bylo motivováno růstem subsystému IP multimedia (IMS) a dalších multimediálních služeb v sítích 3GPP, které vyžadovaly standardizovanou, bezpečnou metodu pro ověřování HTTP Digest a navazování klíčů. Poskytuje flexibilnější a škálovatelnější alternativu k dřívějším metodám, jako je HTTP Digest využívající protokol AKA, tím, že centralizuje správu klíčů v BSF a používá identifikátory jako CSK-ID pro efektivní referenci. Tato architektura je klíčová pro umožnění důvěryhodného poskytování služeb v IoT, službách rich communication a v jakémkoli scénáři, kde je vyžadován vztah důvěry mezi sítí a aplikací.

## Klíčové vlastnosti

- Jednoznačně identifikuje instanci bootstrapovacího relakčního klíče (Ks) mezi UE a BSF
- Umožňuje NAF požádat BSF o službě specifický klíč (Ks_NAF) bez vystavení klíče Ks
- Kryptograficky odvozen z identifikátoru bootstrapovací transakce (B-TID)
- Ústřední prvek procedury GBA pro zabezpečené ověřování na aplikační vrstvě
- Podporuje správu životního cyklu klíčů (např. vypršení platnosti klíče vázané na kontext CSK-ID)
- Zajišťuje izolaci služeb tím, že umožňuje odvodit různé klíče Ks_NAF pro různé NAF ze stejné reference CSK-ID

## Definující specifikace

- **TS 24.380** (Rel-19) — MCPTT Media Plane Control Protocol
- **TS 24.582** (Rel-19) — MCData Media Plane Control Protocols
- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service
- **TS 33.880** (Rel-15) — Security Study for Enhanced Mission Critical Services

---

📖 **Anglický originál a plná specifikace:** [CSK-ID na 3GPP Explorer](https://3gpp-explorer.com/glossary/csk-id/)
